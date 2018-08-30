#!/usr/bin/env python
from __future__ import print_function

import time
import os
import sys
import argparse
import boto3
import json
import logging


class AppRootDirectory(argparse.Action):
    '''custom action class to check if argument is a writable directory'''
    def __call__(self, parser, namespace, values, option_string=None):
        if not os.path.exists(values):
            os.makedirs(values)
        if not os.path.isdir(values):
            raise argparse.ArgumentTypeError(
                "{0}: {1} is not a valid path".format(
                    self.__class__.__name__,
                    values))
        if os.access(values, os.R_OK):
            setattr(namespace, self.dest, values)
        else:
            raise argparse.ArgumentTypeError(
                "{0}: {1} is not a writable dir".format(
                    self.__class__.__name__,
                    values))


def load_metadata():
    '''re-load metadata file until it's ready'''

    metadata_file_path = os.environ.get('ECS_CONTAINER_METADATA_FILE')
    if not metadata_file_path:
        print('ECS_CONTAINER_METADATA_FILE environment variable is not set. '
              'Check ECS agent configuration.')
        sys.exit(1)

    metadata = None
    attempts = 5
    while attempts:
        with open(metadata_file_path, 'r') as metadata_file:
            metadata = json.load(metadata_file)
            if metadata['MetadataFileStatus'] == 'READY':
                return metadata

            print("Waiting for metadata file to become ready")
            time.sleep(1)
            attempts -= 1
    print("Metadata file didn't become ready, exiting.")
    sys.exit(2)


def read_parameters(ssm, names):
    '''read and decrypt parameter values by names list'''
    if not names:
        return {}
    
    parameters = {}
    while len(names) > 0:
        names_lte10 = names[:10]
        del names[:10]

        for p in ssm.get_parameters(
                    Names=names_lte10, WithDecryption=True)['Parameters']:
            name = p['Name'].split('/')[-1]
            parameters[name] = p['Value']

    return parameters


def read_ssm(ssm, root):
    '''enumerate keys under given root and return a map of parameters'''
    describe_parameters = ssm.get_paginator('describe_parameters')
    names = []
    for page in describe_parameters.paginate(Filters=[{'Key':'Name', 'Values': [root]}]):
        names.extend([p['Name'] for p in page['Parameters']])
    return read_parameters(ssm, names)


def main():
    '''bootstrap entry point'''
    ssm = boto3.client('ssm')
    parser = argparse.ArgumentParser(description='SSM Bootstrapper')
    parser.add_argument(
        '-e', '--environ',
        help='Path to use for environ file creation',
        type=argparse.FileType(mode='w'),
        required=True)
    parser.add_argument(
        '-r', '--root',
        help='Path to folder where secret keys should be put',
        action=AppRootDirectory,
        required=True)
    options = parser.parse_args()

    metadata = load_metadata()
    configuration = read_ssm(ssm, '/%s/environment/' % metadata['Cluster'])
    configuration.update(read_ssm(ssm, '/%s/%s/environment/' % (
        metadata['Cluster'],
        metadata['ContainerName'])))
    for key in configuration:
        options.environ.write('export {0}={1}{2}'.format(
            key, configuration[key], os.linesep))

    files = read_ssm(ssm, '/%s/files/' % metadata['Cluster'])
    files.update(read_ssm(ssm, '/%s/%s/files/' % (
        metadata['Cluster'],
        metadata['ContainerName'])))
    for path in files:
        with open(os.path.join(options.root, path), 'w') as f:
            f.write(files[path])

    return 0

if __name__ == '__main__':
    lvl = os.environ.get('LOG_LEVEL') or 'error'
    if lvl == 'error':
        logging.basicConfig(level=logging.ERROR)
    if lvl == 'info':
        logging.basicConfig(level=logging.INFO)
    if lvl == 'debug':
        logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())

#!/usr/bin/env sh
# query SSM parameters store for secrets and save files and environment variables

ssm-bootstrap --environ /tmp/app_environ --root /app/
[ -f /tmp/app_environ ] && . /tmp/app_environ

exec "$@"
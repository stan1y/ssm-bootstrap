ARG BASE
FROM $BASE

RUN apt-get update && \
    apt-get install -y python python-pip python-yaml && \
    pip install awscli && \
    pip install boto3

COPY src/ssm-bootstrap.py /usr/bin/ssm-bootstrap
COPY src/kickstart.sh /usr/bin/kickstart
RUN chmod +x /usr/bin/ssm-bootstrap /usr/bin/kickstart

ENTRYPOINT /usr/bin/kickstart
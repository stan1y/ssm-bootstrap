ARG BASE
FROM $BASE

RUN apt-get update && \
    apt-get install -y python python-pip python-yaml && \
    pip install awscli && \
    pip install boto3 && \
    pip install retry

COPY src/ssm-bootstrap.py src/kickstart.sh /usr/bin/
RUN chmod +x /usr/bin/ssm-bootstrap /usr/bin/kickstart

ENTRYPOINT /usr/bin/kickstart
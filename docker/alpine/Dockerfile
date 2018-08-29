ARG BASE
FROM $BASE

RUN apk update && \
    apk add python \
    apk add python-pip \
    apk add python-yaml \
    pip install awscli \
    pip install boto3

COPY src/ssm-bootstrap.py /usr/bin/ssm-bootstrap
COPY src/kickstart.sh /usr/bin/kickstart
RUN chmod +x /usr/bin/ssm-bootstrap /usr/bin/kickstart

ENTRYPOINT /kickstart
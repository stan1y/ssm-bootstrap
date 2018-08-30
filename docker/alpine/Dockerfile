ARG BASE
FROM $BASE

RUN apk update && \
    apk add python py-pip py-yaml && \
    pip install awscli && \
    pip install boto3 && \
    pip install retry

COPY src/ssm-bootstrap src/kickstart /usr/bin/
RUN chmod +x /usr/bin/ssm-bootstrap /usr/bin/kickstart

ENTRYPOINT /usr/bin/kickstart
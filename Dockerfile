FROM alpine:latest

RUN apk add --no-cache --update python3-dev gcc libc-dev libffi-dev git && \
    ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \
    ln -sf python3 /usr/bin/python && \
    ln -sf pip3 /usr/bin/pip

COPY ./scripts/requirements.txt /tmp

RUN python -m ensurepip && \
    python -m pip install --no-cache --upgrade -r /tmp/requirements.txt

RUN apk add --update --repository http://dl-cdn.alpinelinux.org/alpine/v3.16/main nodejs=16.17.1-r0 npm && \
    apk add --no-cache chromium --repository http://dl-cdn.alpinelinux.org/alpine/v3.16/community

ENV CHROME_BIN=/usr/bin/chromium-browser CHROME_PATH=/usr/lib/chromium

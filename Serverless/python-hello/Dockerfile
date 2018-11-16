FROM python:alpine

ADD https://github.com/alexellis/faas/releases/download/0.9.8/fwatchdog /usr/bin

RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

COPY hello.py .

ENV fprocess="python hello.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]

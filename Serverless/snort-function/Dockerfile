FROM alpine

ADD https://github.com/alexellis/faas/releases/download/0.9.8/fwatchdog /usr/bin
#ADD https://github.com/openfaas-incubator/of-watchdog/releases/download/0.4.1/of-watchdog /usr/bin

RUN    echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories \
    && apk add -Uuv --no-cache snort \
    && apk upgrade -v --available --no-cache

RUN chmod +x /usr/bin/fwatchdog
#RUN chmod +x /usr/bin/of-watchdog

WORKDIR /root/

COPY simple.rules .

RUN touch temp.pcap

#ENV fprocess="cat /dev/stdin | tee temp.pcap && snort -r temp.pcap -e -X -c simple.rules -A console"
#ENV fprocess="cat /dev/stdin | snort -r - -pcap-no-filter  -e -X -c simple.rules -A console"
#ENV fprocess="a=$(</dev/stdin); echo $a"
ENV fprocess="snort -r /dev/stdin -e -X -c simple.rules -A console"

ENV exec_timeout=0
ENV read_timeout=600
ENV write_timeout=600


HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
#CMD ["of-watchdog"]

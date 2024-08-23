ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 py3-pip py3-requests

ENV LANG C.UTF-8

RUN mkdir -p /var/www/html

RUN mkdir /merge-m3u

COPY merge-m3u.py /merge-m3u/
RUN chmod a+x /merge-m3u/merge-m3u.py

COPY run.sh /run.sh
RUN chmod a+x /run.sh

COPY xteve-filtered.m3u /var/www/html/

WORKDIR /var/www/html

# ENTRYPOINT []
CMD [ "/run.sh" ]
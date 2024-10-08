ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 py3-pip py3-requests

ENV LANG C.UTF-8

RUN mkdir -p /var/www/html

RUN mkdir -p /merge-m3u/data && chmod 755 /merge-m3u

COPY merge-m3u.py /merge-m3u/
RUN chmod a+x /merge-m3u/merge-m3u.py

RUN mkdir -p /data/.xteve
WORKDIR /merge-m3u
RUN wget -O xteve.zip "https://github.com/xteve-project/xTeVe-Downloads/blob/master/xteve_linux_amd64.zip?raw=true" && unzip xteve.zip && chmod a+x xteve

COPY run.sh /run.sh

RUN chmod a+x /run.sh

WORKDIR /var/www/html

# ENTRYPOINT []
CMD [ "/run.sh" ]
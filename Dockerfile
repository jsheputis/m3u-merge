ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 py3-pip

ENV LANG C.UTF-8

RUN mkdir -p /var/www/html

RUN mkdir /merge-m3u
WORKDIR /merge-m3u

COPY merge-m3u.py /merge-m3u/
RUN chmod a+x /merge-m3u/merge-m3u.py
COPY requirements.txt /merge-m3u/
RUN pip3 install -r requirements.txt

COPY merge-m3u.py /
RUN chmod a+x /merge-m3u.py

COPY run.sh /
RUN chmod a+x /run.sh

WORKDIR /var/www/html
# ENTRYPOINT []
CMD [ "/run.sh" ]
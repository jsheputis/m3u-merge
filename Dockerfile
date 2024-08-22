ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

ENV LANG C.UTF-8

RUN mkdir -p /var/www/html
WORKDIR /var/www/html
COPY merge-m3u.py /
RUN chmod a+x /merge-m3u.py
# RUN pip3 install -r requirements.txt

COPY livetv.m3u /var/www/html/

COPY run.sh /
RUN chmod a+x /run.sh


# ENTRYPOINT []
CMD [ "/run.sh" ]
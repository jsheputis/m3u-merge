ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

ENV LANG C.UTF-8

RUN mkdir -p /data
WORKDIR /data
COPY merge-m3u.py /
RUN chmod a+x /merge-m3u.py
# RUN pip3 install -r requirements.txt

COPY run.sh /
RUN chmod a+x /run.sh


# ENTRYPOINT []
CMD [ "/run.sh" ]
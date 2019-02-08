FROM python:3.7.2-alpine3.9

# set ports
EXPOSE 8621 62062 6878 8081

RUN apk update && apk add bash
RUN apk add --no-cache bash python3 py3-gevent py-psutil screen nano unzip mc wget tar git && \

# install acestream
wget -o - https://www.dropbox.com/s/blydto9ztkxmf1z/acestream_3.1.33.1_x86_wbUI.tar.gz && \
tar -zxvf acestream_3.1.33.1_x86_wbUI.tar.gz && \
mv acestream.engine/ /opt/ && \

# install aceproxy
wget -o - https://www.dropbox.com/s/sy3qvrtvp60n648/HTTPAceProxy-master.zip && \
unzip HTTPAceProxy-master.zip -d /opt/ && \

# cleanup
rm -rf acestream_3.1.33.1_x86_wbUI.tar.gz HTTPAceProxy-master.zip

ADD start.sh /bash/start.sh
RUN chmod +x /bash/start.sh

CMD ["/bash/start.sh"]

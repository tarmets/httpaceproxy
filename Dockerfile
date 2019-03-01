FROM python:3.8-rc-alpine3.9

# set ports
EXPOSE 8621 62062 6878 8081

RUN apk update && apk add --no-cache bash python3 py3-gevent py-psutil screen nano unzip mc wget tar git tzdata && \

# install acestream
wget -o - https://www.dropbox.com/s/blydto9ztkxmf1z/acestream_3.1.33.1_x86_wbUI.tar.gz && \
tar -zxvf acestream_3.1.33.1_x86_wbUI.tar.gz && \
mv acestream.engine/ /opt/ && \

# install aceproxy
wget -o - https://github.com/pepsik-kiev/HTTPAceProxy/archive/master.zip && \
unzip master.zip -d /opt/ && \

# cleanup
rm -rf acestream_3.1.33.1_x86_wbUI.tar.gz master.zip

ADD add/picons/torrenttv.py /opt/HTTPAceProxy-master/plugins/config/picons/torrenttv.py
ADD add/torrenttelik.py /opt/HTTPAceProxy-master/plugins/config/torrenttelik.py
ADD add/aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD add/torrenttv.py /opt/HTTPAceProxy-master/plugins/config/torrenttv.py
ADD add/playlist.py /opt/HTTPAceProxy-master/modules/playlist.py
ADD start.sh /bash/start.sh
RUN chmod +x /bash/start.sh

CMD ["/bash/start.sh"]

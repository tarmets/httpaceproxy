FROM python:3.8-rc-alpine3.9

# set ports
EXPOSE 8621 62062 6878 8081

RUN apk update && apk add --no-cache bash python3 py3-gevent py-psutil screen nano unzip mc wget tar git tzdata && \

# install acestream
wget -o - https://www.dropbox.com/s/2signb43i8wofv0/acestream_3.1.37_Py2.7.15_webUI_ARMv7.tar.gz && \
tar -zxvf acestream_3.1.37_Py2.7.15_webUI_ARMv7.tar.gz && \
mv acestream.engine/ /opt/ && \

# install aceproxy
wget -o - https://github.com/pepsik-kiev/HTTPAceProxy/archive/master.zip && \
unzip master.zip -d /opt/ && \

# cleanup
rm -rf acestream_3.1.37_Py2.7.15_webUI_ARMv7.tar.gz master.zip

ADD add/aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD add/torrenttv.py /opt/HTTPAceProxy-master/plugins/config/torrenttv.py
ADD add/playlist.py /opt/HTTPAceProxy-master/modules/playlist.py
ADD start.sh /bash/start.sh
RUN chmod +x /bash/start.sh

CMD ["/bash/start.sh"]

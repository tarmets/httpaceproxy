FROM ubuntu:19.10

# time zone data
ENV TZ=Europe/Moscow

# set ports
EXPOSE 8081 62062 6878 8621

# config volume
VOLUME /mnt/films

# update
RUN apt-get update && apt-get upgrade -y

# install apt
RUN apt-get install -y --no-install-recommends \
python3 \
python3-psutil \
python3-gevent \
python-setuptools \
python-m2crypto \
python-apsw \
python-libxslt1 \
sudo \
nano \
mc \
unzip \
wget \
ntp \
unattended-upgrades

# mnt/films
RUN mkdir -p /mnt/films

# install acestream
RUN wget --no-check-certificate https://github.com/tarmets/httpaceproxy/blob/master/add/acestream_3.1.49_ubuntu_18.04_x86_64.zip?raw=true && \
unzip acestream_3.1.49_ubuntu_18.04_x86_64.zip?raw=true -d /opt/

# install aceproxy
RUN wget --no-check-certificate https://github.com/pepsik-kiev/HTTPAceProxy/archive/master.zip && \
unzip master.zip -d /opt/

# clean up
RUN rm -rf acestream_3.1.49_ubuntu_18.04_x86_64.zip?raw=true master.zip && \
apt autoremove -y

# add local files
ADD add/torrenttv.py /opt/HTTPAceProxy-master/plugins/config/torrenttv.py
ADD add/aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD add/acestream.conf /opt/acestream.engine/acestream.conf
ADD add/start.sh /opt/start.sh
RUN chmod +x /opt/acestream.engine/start-engine
RUN chmod +x /opt/acestream.engine/acestreamengine
RUN chmod +x /opt/HTTPAceProxy-master/acehttp.py
RUN chmod +x /opt/start.sh
CMD ["/opt/start.sh"]

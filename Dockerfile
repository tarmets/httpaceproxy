FROM ubuntu:18.10

# set ports
EXPOSE 8621 62062 6878 8081

RUN \
apt-get update && apt-get upgrade -y && \
apt-get install -y \
git \
python3 \
python-pip \
python3.7-gevent \
python3-psutil \
mc \
tar \
unzip \
htop \
wget \
nano && \
apt-get autoremove -y && \


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

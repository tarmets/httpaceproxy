FROM fedora

# set ports
EXPOSE 8621 6878 8081

RUN \
dnf update -yq && \
dnf -y install htop unzip nano mc python3 python3-pip python3-devel wget tzdata && \
dnf -y group install "C Development Tools and Libraries" && \
pip3 install --upgrade psutil && \
pip3 install --upgrade gevent && \

#acestream
wget -o - https://www.dropbox.com/s/blydto9ztkxmf1z/acestream_3.1.33.1_x86_wbUI.tar.gz && \
tar -zxvf acestream_3.1.33.1_x86_wbUI.tar.gz && \
mv acestream.engine/ /opt/ && \
dnf -y autoremove && \

# install aceproxy
wget -o - https://www.dropbox.com/s/sy3qvrtvp60n648/HTTPAceProxy-master.zip -O aceproxy.zip && \
unzip aceproxy.zip -d /opt/ && \

# cleanup
dnf -y remove python3-devel && \
dnf -y group remove "C Development Tools and Libraries" && \
rm -rf acestream_3.1.33.1_x86_wbUI.tar.gz aceproxy.zip

ADD aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD start.sh /bin/start.sh
RUN chmod +x /bin/start.sh

CMD ["/bin/start.sh"]

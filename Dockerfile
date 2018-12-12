FROM fedora

WORKDIR /tmp

# set ports
EXPOSE 8621 9955 62062 6878 8000 8081

# Set a useful default locale
RUN echo "export LANG=ru_RU.utf-8" > /opt/export_LANG.sh
ENV BASH_ENV=/opt/export_LANG.sh \
    ENV=/opt/export_LANG.sh \
    PROMPT_COMMAND="source /opt/export_LANG.sh"

RUN \
dnf -y install fedora-packager rpmdevtools && \
dnf update -yq && \
dnf -y install glibc-langpack-ru* && \
dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-29.noarch.rpm https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-29.noarch.rpm && \
dnf -y install findutils nano htop mc python37 python3-pip python3-devel @development-tools curl wget mc iputils && \
dnf -y group install "C Development Tools and Libraries" && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
python3 get-pip.py && \
pip3 install --upgrade psutil && \
pip3 install setuptools cffi 'cython>=0.27' git+git://github.com/gevent/gevent.git#egg=gevent && \

#acestream
mkdir -p /opt/acestream.engine/ && \
wget -o - https://www.dropbox.com/s/wde2cc3hma9f94f/acestream_3.1.33_x86_webUI.tar.gz && \
tar -zxvf acestream_3.1.33_x86_webUI.tar.gz && \
mv acestream.engine/ /opt/ && \
find /opt/acestream.engine/androidfs/system -type d -exec chmod 755 {} \; && \
find /opt/acestream.engine/androidfs/system -type f -exec chmod 644 {} \; && \
chmod 755 /opt/acestream.engine/androidfs/system/bin/* /opt/acestream.engine/androidfs/acestream.engine/python/bin/python && \
dnf -y remove python3-devel && \
dnf -y group remove "C Development Tools and Libraries" && \
dnf -y autoremove && \
dnf clean packages && \

# install aceproxy
wget -o - https://www.dropbox.com/s/sy3qvrtvp60n648/HTTPAceProxy-master.zip -O aceproxy.zip && \
unzip aceproxy.zip -d /opt/ && \
dnf clean all && \
rm -rf /tmp/* /var/tmp/*

ADD aceconfig.py /opt/HTTPAceProxy-master/aceconfig.py
ADD start.sh /bin/start.sh
ADD acestream.conf /opt/acestream.engine/androidfs/acestream.engine/acestream.conf
RUN chmod +x /bin/start.sh
WORKDIR /

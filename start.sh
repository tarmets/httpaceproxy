#!/bin/sh

/opt/HTTPAceProxy-master/acehttp.py >/dev/null 2>&1 &

while true; do
        sleep 1200
        rm -rf /opt/acestream.engine/androidfs/acestream.engine/.ACEStream/collected_torrent_files/*
done

#!/bin/bash

python3 /opt/HTTPAceProxy-master/acehttp.py >/dev/null 2>&1 &

while true; do
        sleep 1200
        rm -rf /tmp/.ACEStream/collected_torrent_files/*
done

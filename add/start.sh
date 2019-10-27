#!/bin/bash

python3.7 /opt/HTTPAceProxy-master/acehttp.py >/dev/null 2>&1 &

while true; do
        sleep 600
        rm -rf /tmp/.ACEStream/collected_torrent_files/*
done

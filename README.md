# HTTPAceProxy® https://github.com/pepsik-kiev/HTTPAceProxy

# torrent-tv.ru умер!!!
# Плейлисты взяты ACE Search!

# Установка

`docker run -d --net=host -e PGID=0 -e PUID=0 --restart always --privileged --name=aceproxy -e TZ=Europe/Moscow tarmets/httpaceproxy`


# TZ='timezone'

# Для просмотров каналов, используйте ссылку
`http://your_server_ip:8081/torrenttv/playlist.m3u`
# Там где (your_server_ip) вставьте туда свой ip-адрес!

# SYSTEM INFO:
`http://your_server_ip:8081/stat`

# ![screenshot of sample](https://i.ibb.co/B24647m/43434234.jpg)

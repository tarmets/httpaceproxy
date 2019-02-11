# -*- coding: utf-8 -*-
from urllib3.packages.six import ensure_text

class PlaylistConfig():

    # Default playlist format
    m3uemptyheader = '#EXTM3U\n'
    m3uheader = '#EXTM3U deinterlace=1 m3uautoload=1 cache=1000\n'
    # If you need the #EXTGRP field put this #EXTGRP:%(group)s\n after %(name)s\n.
    m3uchanneltemplate = \
       '#EXTINF:-1 group-title="%(group)s" tvg-name="%(tvg)s" tvg-id="%(tvgid)s" tvg-logo="%(logo)s",%(name)s\n#EXTGRP:%(group)s\n%(url)s\n'

    # Playlist sorting options.
    sort = True
    sortByName = True
    sortByGroup = True

    # Channel names mapping. You may use this to rename channels.
    m3uchannelnames = dict()
    # Examples:
    m3uchannelnames['Amedia 1'] = 'A1'
    m3uchannelnames['Amedia 2'] = 'A2'
    m3uchannelnames['Da Vinci Learning'] = 'Da Vinci'
    m3uchannelnames['SET'] = 'Sony channel'
    m3uchannelnames['SET HD'] = 'Sony channel HD'
    m3uchannelnames['History 2 HD'] = 'H2 HD'
    m3uchannelnames['5 канал'] = 'Пятый канал'
    m3uchannelnames['TV XXI (TV21)'] = 'TV XXI'
    m3uchannelnames['TV1000 Action East'] = 'TV 1000 Action'
    m3uchannelnames['TV 1000 Action East'] = 'TV 1000 Action'
    m3uchannelnames['TV1000 Русское кино'] = 'TV 1000 Русское кино'
    m3uchannelnames['Enter Film'] = 'Enter-фильм'
    m3uchannelnames['Кинопоказ 1 HD'] = 'Кинопоказ HD-1'
    m3uchannelnames['Кинопоказ 2 HD'] = 'Кинопоказ HD-2'
    m3uchannelnames['Travel+Adventure'] = 'Travel + adventure'
    m3uchannelnames['Travel + adventure HD'] ='Travel+Adventure HD'
    m3uchannelnames['HD Life'] = 'HDL'
    m3uchannelnames['ID Xtra'] = 'ID Investigation Discovery'
    m3uchannelnames['Первый'] = 'Первый канал'
    m3uchannelnames['ТВ3'] = 'ТВ 3'
    m3uchannelnames['КХЛ'] = 'КХЛ ТВ'
    m3uchannelnames['Канал Disney'] = 'Disney Channel'
    m3uchannelnames['Boomerаng TV'] = 'Boomerаng'
    m3uchannelnames['Nick Jr.'] = 'Nick Jr'
    m3uchannelnames['Бобёр']  = 'Бобер'
    m3uchannelnames['Наука'] = 'Наука 2.0'
    m3uchannelnames['Russian Travel Guide'] = 'RTG TV'
    m3uchannelnames['Иллюзион +'] = 'Иллюзион+'
    m3uchannelnames['РТВ - Любимое кино'] = 'Наше Любимое Кино'
    m3uchannelnames['ТВ Центр'] = 'ТВЦ'
    m3uchannelnames['VH1'] = 'VH1 European'
    m3uchannelnames['1 HD'] = '1HD Music Television'
    m3uchannelnames['1Music (Hungary)'] = '1 Music Channel (Hungary)'

    # Similar to m3uchannelnames but for groups
    m3ugroupnames = dict()
    m3ugroupnames['kids'] = 'Детские'
    m3ugroupnames['music'] = 'Музыка'
    m3ugroupnames['movies'] = 'Фильмы'
    m3ugroupnames['sport'] = 'Спорт'
    #m3ugroupnames[''] = 'Общие'
    m3ugroupnames['educational'] = 'Познавательные'
    m3ugroupnames['informational'] = 'Новостные'
    m3ugroupnames['entertaining'] = 'Развлекательные'
    m3ugroupnames['erotic'] = 'Эротика'
    m3ugroupnames['erotic_18_plus'] = 'Эротика'
    #m3ugroupnames[''] = 'Мужские'
    m3ugroupnames['regional'] = 'Региональные'
    m3ugroupnames['religion'] = 'Религиозные'

    # Channel name to tvg name mappings.
    m3utvgnames = dict()
    # m3utvgnames['Channel name'] = 'Tvg_name'
    m3utvgnames['A1'] = 'Amedia 1'
    m3utvgnames['A2'] = 'Amedia 2'
    m3utvgnames['TV 1000'] = 'TV1000'
    m3utvgnames['TV 1000 HD'] = 'TV1000 HD'
    m3utvgnames['TV 1000 Action'] = 'TV1000 Action'
    m3utvgnames['TV 1000 Action HD'] = 'TV1000 Action HD'
    m3utvgnames['TV 1000 Premium'] = 'TV1000 Premium Baltic'
    m3utvgnames['TV 1000 World Kino'] = 'TV1000 World Kino'
    m3utvgnames['TV 1000 Русское кино'] = 'TV1000 Русское кино'
    m3utvgnames['TV 1000 Русское кино HD'] = 'TV1000 Русское кино'
    m3utvgnames['SET'] = 'Sony channel'
    m3utvgnames['SET HD'] = 'Sony channel HD'
    m3utvgnames['Sony Sci-Fi'] = 'Sony SCI-FI'
    m3utvgnames['A HBO HD'] = 'Amedia Premium HD'
    m3utvgnames['KinoTV Polska'] = 'Kino Polska'
    m3utvgnames['Paramount Comedy HD (Россия)'] = 'Paramount Comedy'
    m3utvgnames['Zee TV Россия'] = 'Zee TV'
    m3utvgnames['Иллюзион+'] = 'Иллюзион +'
    m3utvgnames['КиноПремиум HD'] = 'КиноПремиумHD'
    m3utvgnames['Кинопоказ HD-1'] = 'Шокирующее (Кинопоказ HD-1)'
    m3utvgnames['НСТ'] = 'Настоящее Страшное Телевидение'
    m3utvgnames['Шокирующее HD'] = 'Шокирующее (Кинопоказ HD-1)'
    m3utvgnames['ТВ 3'] = 'ТВ-3 Россия'
    m3utvgnames['HD Life'] = 'HDL'
    m3utvgnames['ID Xtra'] = 'ID Investigation Discovery'
    m3utvgnames['Авто 24'] = 'Авто24'
    m3utvgnames['Дайвинг ТВ HD'] = 'Дайвинг.TV'
    m3utvgnames['Animal Planet'] = 'Animal Planet Россия'
    m3utvgnames['Animal Planet HD'] = 'Animal Planet Россия HD'
    m3utvgnames['Discovery Channel'] = 'Discovery Россия'
    m3utvgnames['Discovery Channel HD'] = 'Discovery Россия HD'
    m3utvgnames['Discovery Historia Polska'] = 'Discovery Historia'
    m3utvgnames['ID Investigation Discovery'] = 'ID Xtra (Россия)'
    m3utvgnames['ID:Investigation Discovery Europe HD'] = 'ID Xtra (Европа)'
    m3utvgnames['HDL'] = 'HDL (HD Life)'
    m3utvgnames['Da Vinci'] = 'Da Vinci Learning Россия'
    m3utvgnames['H2 HD'] = 'H2'
    m3utvgnames['Russia Today Doc.'] = 'RT doc'
    m3utvgnames['Russia Today Doc HD'] = 'RT doc'
    m3utvgnames['Travel + adventure'] = 'Travel+Adventure'
    m3utvgnames['Viasat Explore'] = 'Viasat Explore Россия'
    m3utvgnames['Viasat Nature East'] = 'Viasat Nature'
    m3utvgnames['Viasat Nature-History HD'] = 'Viasat Nature/History HD'
    m3utvgnames['Загородный HD'] = 'Загородный'
    m3utvgnames['Загородный International HD'] = 'Загородный Int'
    m3utvgnames['Зоо ТВ'] = 'Zoo TV (Зоо ТВ)'
    m3utvgnames['Зима'] = 'Зима ТВ (Чебоксары)'
    m3utvgnames['Нано ТВ'] = 'NANO'
    m3utvgnames['Загородный'] = 'Загородный HD'
    m3utvgnames['Россия К'] = 'Россия Культура'
    m3utvgnames['1 Music Channel (Hungary)'] = '1 Music Channel Hungary'
    m3utvgnames['1HD Music Television'] = '1 HD Music Television'
    m3utvgnames['1 MUSIC CHANNEL'] = '1 Music Channel (Romania)'
    m3utvgnames['VH1 European'] = 'VH1 Europe'
    m3utvgnames['Шансон ТВ'] = 'Шансон-ТВ'
    m3utvgnames['5 канал (Украина)'] = '5 канал Украина'
    m3utvgnames['24 Украина'] = '24 (Телеканал новостей 24)'
    m3utvgnames['UA: Буковина'] = 'UA:Буковина'
    m3utvgnames['UA: Одесса'] = 'UA:Одеса (ОДТ)'
    m3utvgnames['UA: Крим'] = 'UA:Крим'
    m3utvgnames['UA: Культура'] = 'UA:Культура'
    m3utvgnames['UA: Перший'] = 'UA:Перший'
    m3utvgnames['UA: TV'] = 'UA:TV'
    m3utvgnames['UA: Житомир'] = 'UA:Житомир'
    m3utvgnames['8 канал'] = '8 канал (Триколор)'
    m3utvgnames['Матч ТВ'] = 'Матч!'
    m3utvgnames['Матч ТВ HD'] = 'Матч!'
    m3utvgnames['Матч! Футбол 1 Резерв 1'] = 'Матч! Футбол 1'
    m3utvgnames['Матч! Футбол 1 Резерв 2'] = 'Матч! Футбол 1'
    m3utvgnames['Матч! Футбол 1 Резерв 3'] = 'Матч! Футбол 1'
    m3utvgnames['Матч! Футбол 1 HD Резерв 1'] = 'Матч! Футбол 1 HD'
    m3utvgnames['Матч! Футбол 1 HD Резерв 2'] = 'Матч! Футбол 1 HD'
    m3utvgnames['Матч! Футбол 1 HD Резерв 3'] = 'Матч! Футбол 1 HD'
    m3utvgnames['Первый канал (4:3)'] = 'Первый канал'
    m3utvgnames['Первый канал (СНГ)'] = 'Первый канал СНГ'
    m3utvgnames['Первый канал Евразия'] = 'Первый канал - Евразия'
    m3utvgnames['Правда тут'] = 'ПравдаТУТ'
    m3utvgnames['РЕН ТВ HD'] = 'РЕН ТВ'
    m3utvgnames['РЕН ТВ Балтийский'] = 'РЕН ТВ Baltic'
    m3utvgnames['Россия HD'] = 'Россия 1 HD'
    m3utvgnames['Мир Премиум HD'] = 'Мир Premium (Мир HD)'
    m3utvgnames['СКИФ (Беларусь)'] = 'СКИФ Витебск'
    m3utvgnames['ТВЦ'] = 'ТВ Центр'
    m3utvgnames['ТВ Центр Международный'] = 'ТВ Центр Международный (TVCI)'
    m3utvgnames['ТВ 3 (Беларусь)'] = 'ТВ3 Беларусь'
    m3utvgnames['11 канал HD (Пенза)'] = '11 канал Наш Дом (Пенза)'
    m3utvgnames['3+ (Латвия)'] = '3+ Latvia'
    m3utvgnames['3+ (Estonia)'] = '3+ Estonia'
    m3utvgnames['360 градусов'] = '360°'
    m3utvgnames['360 градусов HD'] = '360°'
    m3utvgnames['360 Новости'] = '360° Новости'
    m3utvgnames['4 канал HD (Киев)'] = '4 канал Украина (RTi)'
    m3utvgnames['7 канал (Казахстан)'] = '7 канал Казахстан'
    m3utvgnames['7 канал (Одесса)'] = '7 канал Одесса'
    m3utvgnames['8 канал (Беларусь)'] = '8 канал Беларусь'
    m3utvgnames['8 канал (Красноярск)'] = '8 канал Красноярский край'
    m3utvgnames['Armenia 1 Satellite'] = 'Armenia 1 TV Satellite'
    m3utvgnames['Arte Network'] = 'ARTE'
    m3utvgnames['ATV Azerbaycan'] = 'AzTV'
    m3utvgnames['ATV HD'] = 'AzTV'
    m3utvgnames['Blue Hustler'] = 'Blue Hustler Россия'
    m3utvgnames['Brazzers TV Europe'] = 'Brazzers TV Europe (Россия)'
    m3utvgnames['MULTIMANIA TV'] = 'Мультимания'

    # This comparator is used for the playlist sorting.
    @staticmethod
    def sortItems(itemlist):
        if PlaylistConfig.sortByGroup: return sorted(itemlist, key=lambda x:x['group'])
        elif PlaylistConfig.sortByName: return sorted(itemlist, key=lambda x:x['name'])
        else: return itemlist

    # This method can be used to change a channel info such as name, group etc.
    # The following fields can be changed:
    #
    #    name - channel name
    #    url - channel URL
    #    tvg - channel tvg name
    #    tvgid - channel tvg id
    #    group - channel group
    #    logo - channel logo
    @staticmethod
    def changeItem(item):
        PlaylistConfig._changeItemByDict(item, 'name', PlaylistConfig.m3uchannelnames)
        PlaylistConfig._changeItemByDict(item, 'group', PlaylistConfig.m3ugroupnames)
        PlaylistConfig._changeItemByDict(item, 'name', PlaylistConfig.m3utvgnames, 'tvg')

    @staticmethod
    def _changeItemByDict(item, key, replacementsDict, setKey=None):
        if len(replacementsDict) > 0:
           value = item[key]
           if not setKey: setKey = key
           value = replacementsDict.get(value)
           if value: item[setKey] = ensure_text(value)

    xml_template = """<?xml version="1.0" encoding="utf-8"?>
    <items>
    <playlist_name>Playlist</playlist_name>
    %(items)s
    </items>
    """

    xml_channel_template = """
    <channel>
      <title><![CDATA[%(title)s]]></title>
      <description><![CDATA[<tr><td>%(description_title)s</td></tr>]]></description>
      <playlist_url>%(hostport)s%(url)s</playlist_url>
    </channel>
    """

    xml_stream_template = """
    <channel>
      <title><![CDATA[%(title)s]]></title>
      <description><![CDATA[<tr><td>%(description_title)s</td></tr>]></description>
      <stream_url><![CDATA[%(hostport)s%(url)s]]></stream_url>
    </channel>
    """
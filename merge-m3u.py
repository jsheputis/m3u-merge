#!/usr/bin/env python3


import requests
import os

USERNAME = os.getenv('M3U_USERNAME')
PASSWORD = os.getenv('M3U_PASSWORD')

BASE_URL = 'https://tvnow.best/api/list/jsheputis/746923/m3u8'


with open('/data/m3u.m3u', 'w') as outfile:
    contents = requests.get(BASE_URL + '/livetv').text
    outfile.write(contents)
    # for tvshow_num in range(0, 15):
    #     contents = requests.get(BASE_URL + '/tvshows/%d' % tvshow_num).text
    #     outfile.write(contents)
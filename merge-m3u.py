#!/usr/bin/env python3


import requests
import os

USERNAME = os.getenv('M3U_USERNAME')
PASSWORD = os.getenv('M3U_PASSWORD')
BASE_PATH_OVERRIDE = os.getenv('M3U_BASE_PATH')

BASE_URL = 'https://tvnow.best/api/list/%s/%s/m3u8' % (USERNAME, PASSWORD)

BASE_PATH = BASE_PATH_OVERRIDE if None != BASE_PATH_OVERRIDE else '/var/www/html'

print(BASE_URL)
print(BASE_PATH)

try:
    os.remove(BASE_PATH + '/livetv.m3u.wip')
except:
    print("Error in removing livetv.m3u.wip")


# Configure Live TV
with open(BASE_PATH + '/livetv.m3u.wip', 'w') as outfile:
    contents = requests.get(BASE_URL + '/livetv').text
    outfile.write(contents)
    
os.rename(BASE_PATH + '/livetv.m3u.wip', BASE_PATH + '/livetv.m3u')

# Configure Movies
try:
    os.remove(BASE_PATH + '/movies.m3u.wip')
except:
    print("Error in removing movies.m3u.wip")
with open(BASE_PATH + '/movies.m3u.wip', 'w') as outfile:
    contents = requests.get(BASE_URL + '/movies').text

    outfile.write(contents)

os.rename(BASE_PATH + '/movies.m3u.wip', BASE_PATH + '/movies.m3u')


# Configure TV Shows
try:
    os.remove(BASE_PATH + '/tvshows.m3u.wip')
except:
    print("Error in removing tvshows.m3u.wip")
with open(BASE_PATH + '/tvshows.m3u.wip', 'w') as outfile:


    for tvshow_num in range(0, 15):
        contents = requests.get(BASE_URL + '/tvshows/%d' % tvshow_num).text
        outfile.write(contents)
    
os.rename(BASE_PATH + '/tvshows.m3u.wip', BASE_PATH + '/tvshows.m3u')
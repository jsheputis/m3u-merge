#!/usr/bin/env python3


import requests
import os
import re
from pathlib import Path
import urllib.request

USERNAME = os.getenv('M3U_USERNAME')
PASSWORD = os.getenv('M3U_PASSWORD')
BASE_PATH_OVERRIDE = os.getenv('M3U_BASE_PATH')
WORKING_SPACE_DIR_BASE_PATH_OVERRIDE = os.getenv('M3U_WORKING_SPACE_DIR_BASE_PATH')

# BASE_URL = 'https://tvnow.best/api/list/%s/%s/m3u8' % (USERNAME, PASSWORD)
BASE_URL = 'http://xkdhhfy.mmastertv.xyz/get.php?username=%s&password=%s&output=ts&type=m3u_plus' % (USERNAME, PASSWORD)

BASE_PATH = BASE_PATH_OVERRIDE if None != BASE_PATH_OVERRIDE else '/var/www/html'
WORKING_SPACE_DIR_BASE_PATH_OVERRIDE = WORKING_SPACE_DIR_BASE_PATH_OVERRIDE if None != WORKING_SPACE_DIR_BASE_PATH_OVERRIDE else '/m3u-merge/data'

EPG_URL = 'https://epgshare01.online/epgshare01/epg_ripper_US1.xml.gz'

HEADERS = {
    'User-Agent': 'M3U',
    'Accept': '*/*',
    'Connection': 'Keep-Alive'
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'M3U')]
urllib.request.install_opener(opener)

print("Configuring workspace...")
print(WORKING_SPACE_DIR_BASE_PATH_OVERRIDE)
Path(WORKING_SPACE_DIR_BASE_PATH_OVERRIDE).mkdir(parents=True, exist_ok=True)

# TODO: Put in loop and update periodically

print("Processing M3U data...")
REGEX_TEST = re.compile('#EXTINF.*?tvg-id=".*\.us"')
with open(WORKING_SPACE_DIR_BASE_PATH_OVERRIDE + '/all-simplified.m3u.wip', 'w') as outfile:
    contents = requests.get(BASE_URL, headers=HEADERS).text.splitlines()
    print("File read. %d records." % len(contents))
    
    outfile.write(contents[0]) # Header line
    outfile.write('\n')
    i = 1
    total = len(contents)

    while i < total - 2:
        headerline = contents[i]
        dataline = contents[i+1]
        if 'WEST' not in headerline and re.match(REGEX_TEST, headerline) is not None:
            outfile.write(headerline)
            outfile.write('\n')
            outfile.write(dataline)
            outfile.write('\n')
        i = i+1


os.rename(WORKING_SPACE_DIR_BASE_PATH_OVERRIDE + '/all-simplified.m3u.wip', BASE_PATH + '/all-simplified.m3u')
print("M3U File creation complete.")

def getGuideData():
    urllib.request.urlretrieve(EPG_URL, WORKING_SPACE_DIR_BASE_PATH_OVERRIDE + '/xmltv.xml.gz.wip')
    os.rename(WORKING_SPACE_DIR_BASE_PATH_OVERRIDE + '/xmltv.xml.gz.wip', BASE_PATH + '/xmltv.xml.gz')
print("Processing XMLTV data...")
try:
    getGuideData()
    print("XMLTV File creation complete.")
except:
    print("Error getting guide data...")

# # Configure Movies
# try:
#     os.remove(BASE_PATH + '/movies.m3u.wip')
# except:
#     print("Error in removing movies.m3u.wip")
# with open(BASE_PATH + '/movies.m3u.wip', 'w') as outfile:
#     contents = requests.get(BASE_URL + '/movies').text

#     outfile.write(contents)

# os.rename(BASE_PATH + '/movies.m3u.wip', BASE_PATH + '/movies.m3u')


# # Configure TV Shows
# try:
#     os.remove(BASE_PATH + '/tvshows.m3u.wip')
# except:
#     print("Error in removing tvshows.m3u.wip")
# with open(BASE_PATH + '/tvshows.m3u.wip', 'w') as outfile:


#     for tvshow_num in range(0, 15):
#         contents = requests.get(BASE_URL + '/tvshows/%d' % tvshow_num).text
#         outfile.write(contents)

# os.rename(BASE_PATH + '/tvshows.m3u.wip', BASE_PATH + '/tvshows.m3u')
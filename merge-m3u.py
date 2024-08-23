#!/usr/bin/env python3


import requests
import os
import re

USERNAME = os.getenv('M3U_USERNAME')
PASSWORD = os.getenv('M3U_PASSWORD')
BASE_PATH_OVERRIDE = os.getenv('M3U_BASE_PATH')

# BASE_URL = 'https://tvnow.best/api/list/%s/%s/m3u8' % (USERNAME, PASSWORD)
BASE_URL = 'http://xkdhhfy.mmastertv.xyz/get.php?username=%s&password=%s&output=ts&type=m3u_plus' % (USERNAME, PASSWORD)

BASE_PATH = BASE_PATH_OVERRIDE if None != BASE_PATH_OVERRIDE else '/var/www/html'

HEADERS = {
    'User-Agent': 'M3U',
    'Accept': '*/*',
    'Connection': 'Keep-Alive'
}

print(BASE_URL)
print(BASE_PATH)

# try:
#     os.remove(BASE_PATH + '/all.m3u.wip')
# except:
#     print("Error in removing all.m3u.wip")

# contents = requests.get(BASE_URL, headers=HEADERS, stream=True)
# for line in contents.iter_lines():
#     print(line)
#     exit(0)
# # Configure Live TV

REGEX_TEST = re.compile('#EXTINF.*?tvg-id=".*\.us"')
with open(BASE_PATH + '/all.m3u.wip', 'w') as outfile:
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


os.rename(BASE_PATH + '/all.m3u.wip', BASE_PATH + '/all2.m3u')

print("File creation complete.")
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
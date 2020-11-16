#!/usr/bin/python

import pafy
import time
import sys
import shutil
import subprocess
import os
import zipfile
import datetime as dt

os.system('color')

now = dt.datetime.now()

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\u001b[1m",
}

print('The playlist' +  COLOR['RED'], 'MIGHT' + COLOR['ENDC'], 'not download correctly with private or deleted videos.')
url = input('What playlist do you want to save?: ')
download = input('Do you want to download the playlist? (type Y/N): ')
if download not in ('Y', 'N'):
    while True:
        download = input('Do you want to download the playlist? (type Y/N): ')
        if download not in ('Y', 'N'):
            continue
        else:
            break
else:
    pass

# makes a dict of playlist metadata
try:
    playlist = pafy.get_playlist(url)
except:
    print('This playlist does not exist.')
    time.sleep(2)
    sys.exit()

items = playlist['items']
x = 0
urlLIST = []

# writing playlist title
with open('links.txt', 'a') as link:
    link.write(playlist['title'])
    link.close()

# writing each video url
for i in range(len(playlist['items'])):
    item = items[x]
    x = x + 1
    metadata = item['playlist_meta']
    value = metadata['encrypted_id']
    urlLIST.append('https://youtube.com/watch?v=' + value)
    with open('links.txt', 'a') as link:
        link.write('\n')
        link.writelines('https://youtube.com/watch?v=' + value)
        link.close()

if download == 'Y':
    try:
        PATH = input("Where do you want to download the playlist?: ")
        proc = subprocess.run(['youtube-dl.exe', '-ci', url], stdout=subprocess.PIPE, shell=True)
        print(COLOR['GREEN'], 'Download Successful.\n', COLOR['ENDC'] + 'Zipping files...')
        my_zip = zipfile.ZipFile(playlist['title'] + '.zip', 'w', compression=zipfile.ZIP_DEFLATED)
        pyPATH = os.getcwd()
        for file in os.listdir(pyPATH):
            if file.endswith('.mp4'):
                my_zip.write(file)
                os.remove(file)
            else:
                pass
        my_zip.close()
        print(pyPATH)
        shutil.move(pyPATH + '\\' + playlist['title'] + '.zip', PATH)
        print(COLOR['GREEN'], 'Zipping Complete.\n', COLOR['ENDC'] + 'Exiting...')
        time.sleep(2)
        sys.exit()
    except:
        print(COLOR['RED'], 'Unexpected error occured.')
        print(COLOR['RED'], 'Exiting.')
        time.sleep(2)
        sys.exit()
else:
    pass
sys.exit()

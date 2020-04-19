# Created by Yifei Chen on 04/18/2020 at 4:47 PM
import os
from urllib import request

import requests
from bs4 import BeautifulSoup
import time

paths = []
h = os.walk(r"/Volumes/Samsung/Music ready to roll/豆瓣音乐top250 FLAC分轨")
for path, dir_list, file_list in h:
    for dir_name in dir_list:
        paths.append(os.path.join(path, dir_name))
paths.sort()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
cnt = 0


def get_url_music(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    music_hrefs = soup.select('a.nbg')
    for music_href in music_hrefs:
        get_music_info(music_href['href'])
        time.sleep(2)


def get_music_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    image = soup.select('a.nbg')[0]['href']
    global cnt
    # os.mkdir(f'/Users/ychen/Documents/Pics/{cnt}/')
    picname = paths[cnt] + '/cover.jpg'
    cnt += 1
    request.urlretrieve(image, filename=picname)


for url in urls:
    get_url_music(url)

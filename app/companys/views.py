import json
import os
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

from config.settings import BASE_DIR

def crawling():
    url = 'http://www.welkeepsmall.com/shop/shopbrandCA.html?type=X&xcode=023'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    mask_list = []

    mask_all_info = soup.select(".info")
    # print(mask_all_info)

    mask_text_list = []
    for mask in mask_all_info:
        mask_text_list.append(mask.get_text())

    list_len = len(mask_text_list)

    for mask in range(list_len):
        mask_list.append(mask_text_list[mask].split('\n'))

    for mask in mask_list:
        del mask[0]

    # 최종 가공된 버전 mask

    print(mask_list)
    # print(mask_text_list[0].split('\n'))
    # print(mask_text_list[1].split('\n'))

crawling()

# data = {}

# result.json에 저장하기

# with open(os.path.join(BASE_DIR, 'result.json')) as json_file:
#     json.dump(data, json_file)
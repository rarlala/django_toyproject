import json
import os
import re
import requests
from bs4 import BeautifulSoup
import urllib.request

from django.core.mail import send_mail
from companys.models import Info, Mask_Info
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

    for num in range(list_len):
        name = (mask_list[num])[0]
        desc = (mask_list[num])[1]
        soldout = (True if (mask_list[num])[2] == "SOLD OUT"  else False)
        price = (mask_list[num])[3]

        Mask_Info.objects.get_or_create(name=name ,desc= desc,price=price,soldout=soldout)

crawling()




send_mail(
    '웰킵스 구매 가능!',
    '마스크 구매가능',
    'welkeeps.service@gmail.com',
    ['wtw9611@gmail.com'],
    fail_silently=False,
)
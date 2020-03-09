import json, os, re, requests
from bs4 import BeautifulSoup
import urllib.request

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from companys.models import Mask_Info

def crawling():
    # Mask_Info.objects.all().delete()

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

    # 구매 가능한 마스크
    buy_mask = []

    for num in range(list_len):
        name = (mask_list[num])[0]
        desc = (mask_list[num])[1]
        soldout = (True if (mask_list[num])[2] == "SOLD OUT" else False)
        price = (mask_list[num])[3]

        Mask_Info.objects.get_or_create(name=name, desc=desc, price=price, soldout=soldout)

        buy_mask_list = Mask_Info.objects.filter(soldout=0).values('name')

    for buy in buy_mask_list:
        buy_mask.append(buy['name'])

    print('buy_mask', buy_mask)
    print('if buy_mask != []', buy_mask != [])
    print('if buy_mask == []', buy_mask == [])
    print('buy_mask str', str(buy_mask))
    print('buy_mask str type', type(str(buy_mask)))

    if buy_mask != []:
        print('메일 발송')
        # send_email('wtw9611@gmail.com', str(buy_mask))
        # send_mail(
        #     '[안내 메일]웰킵스 구매 가능!',
        #     'buy_mask 마스크 구매가능',
        #     'welkeeps.service@gmail.com',
        #     ['wtw9611@gmail.com'],
        #     fail_silently=False,
        # )


# def send_email(email, buy_mask):
#     subject = '[안내] 웰킵스 마스크 구매 가능!'
#     from_email = 'welkeeps.service@gmail.com'
#     to = 'wtw9611@gmail.com'
#     text_content = '마스크 구매 가능합니다.'
#     html_content = '<p> <strong>웰킵스 마스크 구매 가능 안내</strong> 메일입니다.</p>' \
#                    '<small style="font-color:gray">이 메일은 웰킵스 안내 서비스에 가입하신 고객님께 보내드리는 메일입니다.</small>' \
#             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#

crawling()

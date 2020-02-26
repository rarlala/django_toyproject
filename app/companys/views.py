import requests
from bs4 import BeautifulSoup
import urllib.request


def crawling():
    url = 'http://www.welkeepsmall.com/shop/shopbrandCA.html?type=X&xcode=023'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    mask_info = soup.select(".info")


crawling()

def data_save():
    Info()
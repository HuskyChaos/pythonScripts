#!/bin/python

from distutils.filelist import findall
from gettext import find
import urllib.request
from bs4 import BeautifulSoup
from bs4 import Comment


def urlCheck(url):
    if 'http://' not in url or 'https://' not in url:
        url = 'http://' + url
        openUrl(url)
    else:
        openUrl(url)

def openUrl(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        print("========= Links =========")

        for a in soup.find_all('a'):
            print(a['href'])

        print("========= Comments =========")

        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        print(comments)

try:
    url = input()
    urlCheck(url)

except Exception as e:
    print(e)

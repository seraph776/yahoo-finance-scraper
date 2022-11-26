#!/usr/bin/env python3
"""
created: 2022-11-25
@author: seraph1001100
project: Yahoo Finance
"""
import requests
from bs4 import BeautifulSoup
import config
import os


def get_download_link(symbol):
    url = config.BASEURL + f'/quote/{symbol}/history'
    try:
        r = requests.get(url=url, headers=config.HEADERS)
    except requests.RequestException as e:
        raise SystemExit(e)
    soup = BeautifulSoup(r.text.encode('utf8'), 'lxml')
    try:
        return soup.find('a', attrs={'download': f'{symbol.upper()}.csv'}).attrs['href']
    except AttributeError as e:
        print('Item does not have  download link')


def download_financial_data(link, filename):
    r = requests.get(link, stream=True, headers=config.HEADERS)
    path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(path):
        os.mkdir(path)
    with open(os.path.join(path, filename), 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)
        print(f'{filename} has been written!')
        return True
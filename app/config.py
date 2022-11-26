#!/usr/bin/env python3
"""
created: 2022-11-25
@author: seraph1001100
project: Yahoo Finance
"""
from fake_useragent import FakeUserAgent

USERAGENT = FakeUserAgent().random
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': USERAGENT,
}

BASEURL = 'https://finance.yahoo.com'
SYMBOLS = [ 'AMZN', 'AAPL', 'GOOG', 'NFLX', 'META', 'TSLA', 'BTC-USD','ETH-USD']




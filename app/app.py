#!/usr/bin/env python3
"""
created: 2022-11-25
@author: seraph1001100
project: Yahoo Finance
"""
import aux
import config

if __name__ == '__main__':

    for i, symbol in enumerate(config.SYMBOLS):
        link = aux.get_download_link(symbol)
        aux.download_financial_data(link, f'{symbol.upper()}.csv')
        print(f'Saving file #{i}\n')
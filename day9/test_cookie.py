# -*- coding: utf-8 -*-
import requests

url = 'https://www.kxdao.net'

headers = {
    'cookie': 'G1NZ_2132_saltkey=vwRhDroI;G1NZ_2132_auth=a19aJ3I7h51sYEEzxrWDLZuG0Y3AlNxC%2FH7%2FsKfbx%2BFRT%2BRdXLfchEetKRebvn8MkuOz2DzEs26qAB2J2zAJxGwVGQ',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

html = requests.get(url=url, headers=headers)

print(html.text)


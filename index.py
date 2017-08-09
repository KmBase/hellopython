from unittest import result
import requests
import os, sys
from bs4 import BeautifulSoup

for i in range(20,30):
    url = 'http://www.sxmwr.gov.cn/List.action?classfyid=61&currentPage=' + str(i) + '&turnHref=a0909d3e2591f4bad185dcc317ed1305ecd1ce6e561ebba08b16ce55831d5ab8a287dfa4a19beda0c6bc579659449f995714cf0f1d6601099d111aa8b2a942c122565fccc10321a12fa3875b48a46949d5c36fb26f106d16e54a688e17199bd5c4e6b68a622d3b2792ba2c781a2d4e17fffe1f9e8c4d6cdf6348d9a80dbcf0bdaea67d6bcc745b348c230d59c63a6576131bcee30514c0527ad244d7662c1922'
    res = requests.get(url)
    res.encoding = 'utf-8'
    html_sample = res.text
    soup = BeautifulSoup(html_sample, 'html.parser')
    for link in soup.select('.articlelist'):
        s=(link)
        soup2 = BeautifulSoup(str(s), 'html.parser')
        alinks = soup2.select('a')
        for links in alinks:
            print(links['href'])
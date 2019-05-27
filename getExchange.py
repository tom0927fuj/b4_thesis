# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv
from time import sleep

#domain="https://coin.market"
domain="https://coinmarketcap.com"
#domain="https://www.worldcoinindex.com"
# アクセスするURL
#url = "https://coin.market/exchanges-info.php?what="
url="https://coinmarketcap.com/exchanges/volume/24-hour/"
#url="https://www.worldcoinindex.com/exchange"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(req)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, 'lxml')
#soup = BeautifulSoup(html,"html.parser")

#tables = soup.findAll('table', class_='table table-hover exch-table')
tables = soup.findAll('table', class_='table table-condensed border-top')
#tables = soup.findAll('table', id='market-table')

# 第一引数: 取得したいタグの指定、class_: クラス属性の指定
abs_link=[];
name=[];

for table in tables:
    #for tr in table.findAll('tr'):
    for tr in table.findAll('h3', class_='padding-top--lv6 margin-bottom--lv2'):
    #for tr in table.findAll('tr'):
        for link in tr.find_all('a'):
            rel_link=link.get('href')
            if rel_link!="#":
                abs_link.append(domain+rel_link)
                name.append(link.text)
name_link=[];
"""
for ablink in abs_link:
    req = urllib.request.Request(ablink, headers={'User-Agent': 'Mozilla/5.0'})
    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(req)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find('table', class_='table table-hover market_statistics descrip_table zebra mt-4')
    a_table=tables.find('a')
    name_link.append(a_table.get('href'))
    print(a_table.get('href'))
"""

for ablink in abs_link:
    print(ablink)
    try:
        #chaoex
        sleep(5)
        req = urllib.request.Request(ablink, headers={'User-Agent': 'Mozilla/5.0'})
        # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
        html = urllib.request.urlopen(req)
        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html, 'lxml')
        tables = soup.find('div', class_='col-xs-12')
        a_table=tables.find('a')
        name_link.append(a_table.get('href'))
    except:
        print("error:%s",ablink)
    #print(a_table.get('href'))

"""
for ablink in abs_link:
    req = urllib.request.Request(ablink, headers={'User-Agent': 'Mozilla/5.0'})
    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(req)
    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find('div', class_='volumeContainer1 volume exchangeCoinContainer')
    a_table=tables.find('a')

    name_link.append(a_table.get('href'))
    print(a_table.get('href'))
"""
print(name_link)

list=[];
count=len(name_link)
for i in range(count):
    list.append([i,name[i],name_link[i]])

print(list)



f = open('url20181224-02.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(list)
f.close()

# タイトル要素を出力
#print(tables)

# タイトルを文字列を出力
#print(title)

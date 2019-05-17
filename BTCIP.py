# coding: utf-8
import csv
import codecs
import pandas as pd
import io,sys
import requests
import json
import re
import time
from datetime import datetime

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='ignore')
nm="20181122102831"
inputname="Timestamp"+nm+".csv"
df = pd.read_csv(inputname, header=None)
timestamp_list = df.iloc[:,0].values

ip_list=[]

time=datetime.now()
year=time.strftime('%Y%m%d%H%M%S')

inputname="BtcIP"+nm+".csv"
df2 = pd.read_csv(inputname, header=None)
lista=df2.iloc[:,0].values
for idx,ts in enumerate(lista):
    if ts=="1541971635":
        break;
    ip_list.append(ts)
print(ip_list)

#fname = "BtcIP"+year+".csv"
fname="BtcIP20181113172820.csv"
fw = codecs.open(fname, 'a', "utf-8")


#正規表現
regex = '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
regex2 = '[a-xA-Z0-9]*.onion.*[a-xA-Z0-9]*'

for idx,ts in enumerate(timestamp_list,290):
    print(idx)
    api = "https://bitnodes.earn.com/api/v1/snapshots/{key}/"
    url = api.format(key=ts)
    r = requests.get(url)
    data = json.loads(r.text)
    nodes3=data['nodes']
    OnionCount=0
    for idx2,p in enumerate(data['nodes']):
        matchObj = re.match(regex,p)
        iswrite = False
        #fw.write("%s,," % (p))
        if idx==0:
            if matchObj != None:
                ip_list.append(matchObj.group(0))
                fw.write("%s," % (matchObj.group(0)))
                iswrite=True
        else:
            if matchObj != None:
                isIP=False
                for idx2,ip2 in enumerate(ip_list):
                    if ip2==matchObj.group(0):
                        isIP=True
                if isIP==False:
                    ip_list.append(matchObj.group(0))
                    fw.write("%s," % (matchObj.group(0)))
                    print(matchObj.group(0))
                    iswrite=True
        if iswrite:
            fw.write("\r")
"""
#pagemax=1567
pagemax=800
for i in range(pagemax):
    print(i)
    page2=i+1
    # 最新のtimestampを取得
    api="https://bitnodes.earn.com/api/v1/snapshots/?page={page}"
    url = api.format(page=page2)
    # 実際にAPIにリクエストを送信して結果を取得する
    r1 = requests.get(url)
    # 結果はJSON形式なのでデコードする
    data1 = json.loads(r1.text)
    fullsnap=data1['results']
    apikey=[]
    for idx,p in enumerate(fullsnap):
        apikey.append(p['timestamp'])
        fw.write("%d," % (p['timestamp']))
        fw.write("\n")
fw.close()
"""
"""
timenow=datetime.fromtimestamp(apikey)
fw.write("%s,%s\r" % (apikey,timenow))
#最新のtimestampのノード情報を取得
api = "https://bitnodes.earn.com/api/v1/snapshots/{key}/"
url = api.format(key=apikey)
r = requests.get(url)
data = json.loads(r.text)
nodes3=data['nodes']
OnionCount=0
for idx,p in enumerate(data['nodes']):
    matchObj = re.match(regex,p)
    matchObj2 = re.match(regex2,p)
    iswrite = False
    #fw.write("%s,," % (p))
    if matchObj != None:
        fw.write("%s," % (matchObj.group(0)))
        iswrite=True
    if matchObj2 != None:
        OnionCount+=1
    for idx2,pp in enumerate(nodes3[p]):
        if iswrite:
            if idx2 in {5,6,11,12}:
                str(pp).replace(",", " ")
                fw.write("%s," % (pp))
    if iswrite:
        fw.write("\r")
    #else:
    #    fw.write("\r")

fw.write(",%d\r" % (OnionCount))
"""
"""
for idx,p in enumerate(data['results']):
    fw.write("%d," % (p['timestamp']))
    apikey=p['timestamp']
    api = "https://bitnodes.earn.com/api/v1/snapshots/{key}/"
    url = api.format(key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする
    data2 = json.loads(r.text)
    matchObj = re.match(regex, r.text)
    fw.write("%s\r" % (matchObj))
"""

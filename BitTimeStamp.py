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
import os.path

time=datetime.now()
year=time.strftime('%Y%m%d%H%M%S')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='ignore')

fname = "Timestamp"+year+".csv"

#fw=open(fname,'w')
fw = codecs.open(fname, 'w', "utf-8")

#正規表現
regex = '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
regex2 = '[a-xA-Z0-9]*.onion.*[a-xA-Z0-9]*'

pagemax=1300
#pagemax=100
for i in range(pagemax):
    if i%100==0:
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
    fw.write("%d\n" % (fullsnap[0]['timestamp']))
    fw.write("%d\n" % (fullsnap[2]['timestamp']))
    fw.write("%d\n" % (fullsnap[4]['timestamp']))
    fw.write("%d\n" % (fullsnap[6]['timestamp']))
    fw.write("%d\n" % (fullsnap[8]['timestamp']))
    """
    apikey=[]
    for idx,p in enumerate(fullsnap):
        apikey.append(p['timestamp'])
        fw.write("%d," % (p['timestamp']))
        fw.write("\n")
    """
fw.close()

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

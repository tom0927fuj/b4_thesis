# coding: utf-8
import csv
import codecs
import pandas as pd
import io,sys
import requests
import json
import re
import socket
import time
from datetime import datetime
import os.path

time=datetime.now()
year=time.strftime('%Y%m%d%H%M%S')

fname2="RippleIpList.csv"
#fw=open(fname,'w')

df2 = pd.read_csv(fname2, header=None)
iplist = df2.iloc[:,0].values

fw2 = codecs.open(fname2, 'a', "utf-8")

os.chdir('./out/ripple')
na="RippleOutIP-"+year+".csv"
#fname=os.path.join(os.getcwd(),"out",na)
fw = codecs.open(na, 'w', "utf-8")

# 最新のtimestampを取得
api="https://data.ripple.com/v2/network/topology/nodes?verbose=true&limit=100000"
# 実際にAPIにリクエストを送信して結果を取得する
r1 = requests.get(api)
# 結果はJSON形式なのでデコードする
data1 = json.loads(r1.text)
apikey=data1['nodes']
for idx,p in enumerate(apikey):
    try:
        host=p['ip']
        try:
            country2=p['country']
            country = re.sub(',', ' ', country2)
        except:
            country="NONE"
        try:
            isp2=p['isp']
            isp=re.sub(',', ' ', isp2)
        except:
            isp="NONE"
        fw.write("%s,%s,%s\n" % (host,country,isp))
        isWrite=False
        for idx2,p2 in enumerate(iplist):
            if host == p2:
                isWrite=True
                break
        if isWrite==False:
            print("write:",host)
            fw2.write("%s\n" %(host))
    except:
        host="NONE"

fw.close()
fw2.close()

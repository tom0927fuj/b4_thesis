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

fname2="EtherIpList.csv"
df2 = pd.read_csv(fname2, header=None)
iplist = df2.iloc[:,0].values

fw2 = codecs.open(fname2, 'a', "utf-8")

os.chdir('./out/ether')
na="EtherOutIP-"+year+".csv"
#fname=os.path.join(os.getcwd(),"out",na)
fw = codecs.open(na, 'w', "utf-8")

#正規表現
regex = '[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
regex2 = '[a-xA-Z0-9]*.onion.*[a-xA-Z0-9]*'

# 最新のtimestampを取得
api="https://www.ethernodes.org/network/1/data?draw=1&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=host&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=port&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=country&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=clientId&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&"
api+="columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=client&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=clientVersion&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=os&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=lastUpdate&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&"
api+="columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=25000&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1542094767897"
# 実際にAPIにリクエストを送信して結果を取得する
r1 = requests.get(api)
# 結果はJSON形式なのでデコードする
data1 = json.loads(r1.text)
apikey=data1['data']
for idx,p in enumerate(apikey):
    host=p['host']
    country2=p['country']
    country = re.sub(',', ' ', country2)
    matchObj = re.fullmatch(regex,host)
    if matchObj != None:
        fw.write("%s,%s\n" % (host,country))
        isWrite=False
        for idx2,p2 in enumerate(iplist):
            if host == p2:
                isWrite=True
                break
        if isWrite==False:
            print("write:",host)
            fw2.write("%s\n" %(host))
    else:
        try:
            ip_adders = socket.gethostbyname_ex(host)
            for idx2,ip_ad in enumerate(ip_adders[2]):
                fw.write("%s,%s\n" % (ip_ad,country))
                isWrite=False
                for idx2,p2 in enumerate(iplist):
                    if ip_ad == p2:
                        isWrite=True
                        print(ip_ad,p2)
                        break
                if isWrite==False:
                    print("write:",ip_ad)
                    fw2.write("%s\n" %(ip_ad))
        except:
            error="ERROR"
            fw.write("%s,%s,%s\n" % (host,country,error))

"""
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
fw.close()
fw2.close()

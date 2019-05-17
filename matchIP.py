# coding: utf-8
import csv
import ipaddress
import pandas as pd
import codecs
import socket
import sys
import re

if(__name__ == "__main__"):

    inputname="InExchanges20181224.csv"
    with codecs.open(inputname, 'r', 'utf-8', 'ignore') as f:
        df = pd.read_csv(f)
    ip_list = df.iloc[:,4].values

    inputname2="BTCIP1112-1231.csv"
    #inputname2="EtherIpList.csv"
    #inputname2="RippleIpList.csv"
    #inputname2="OutRippleIP-1112.csv"
    df2 = pd.read_csv(inputname2, header=None)
    peer_list = df2.iloc[:,0].values
    print(len(peer_list))
    fname = "OutPeerResult1112-1231BTC.csv"
    #fname = "OutPeerResult1112-1231Ether.csv"
    #fname = "OutPeerResult1112-1231Ripple.csv"
    fw = open(fname, 'w')
    fw.write("No,Exchange,URL,IP_Adder,Peer\n")

    peer_size=len(peer_list)

    tr='MATCH'
    tr2='-'

    for idx,ip in enumerate(ip_list):
        print("\r %d / %d" % (idx, len(ip_list)-1))
        ip_sp=ip.split('.')
        ip_third=0
        fw.write("%s,%s,%s,%s," % (df.iloc[idx,0],df.iloc[idx,1],df.iloc[idx,2],ip))
        for idx2,peer in enumerate(peer_list):
            peer_sp=peer.split('.')
            try:
                if ipaddress.IPv4Address(ip) == ipaddress.IPv4Address(peer):
                    fw.write("%s\n" % (tr))
                    print("true")
                    break
                if ((ip_sp[0]==peer_sp[0])and(ip_sp[1]==peer_sp[1])and(ip_sp[2]==peer_sp[2])):
                    ip_third=peer
                    print(peer)
                elif (idx2+1)==peer_size:
                    if ip_third==0:
                        fw.write("%s\n" % (tr2))
                    else:
                        fw.write("%s," % (tr2))
                        fw.write("%s\n" % (ip_third))
            except:
                g=0

fw.close()

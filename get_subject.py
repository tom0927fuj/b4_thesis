import pandas as pd
import socket
import sys
import ssl
from time import sleep
import OpenSSL
import pygeoip
import geoip2.database
import re

if(__name__ == "__main__"):
    inputname="Exchanges20181224.csv"
    df = pd.read_csv(inputname)
    ip_list = df.iloc[:,4].values

    fname = "OutSubjectResult20181224.csv"
    fw = open(fname, 'w')
    fw.write("No,Exchange,URL,IP_Adder,Subject\n")
    bef_ip=""
    bef_sub=""
    for idx,ip_ad in enumerate(ip_list):
        print("\r %d / %d" % (idx, len(ip_list)-1))
        fw.write("%s,%s,%s,%s," % (df.iloc[idx,0],df.iloc[idx,1],df.iloc[idx,2],ip_ad))
        if(bef_ip!=ip_ad):
            try:
                sleep(2)
                cert = ssl.get_server_certificate((ip_ad, 443))
                x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
                cert_subject=x509.get_subject()
                print(cert_subject)
                fw.write("%s\n" % (cert_subject))
                bef_ip=ip_ad
                bef_sub=cert_subject
            except:
                fw.write("error\n")
        else:
            fw.write("%s\n" % (cert_subject))
    #
    fw.close()

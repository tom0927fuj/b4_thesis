# coding: utf-8
import pandas as pd
import socket
import sys
import ssl
import OpenSSL
import codecs
import pygeoip
import geoip2.database
import re

if(__name__ == "__main__"):

    # Set params
    input_path = "../data/"
    output_dir = "../out/"
    inputname="url20181224.csv"
    #inputname="InExchangeJapan.csv"
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    #giisp = pygeoip.GeoIP('GeoIPISP.dat')
    giasn = pygeoip.GeoIP('GeoIPASNum.dat')

    with codecs.open(inputname, 'r', 'utf-8', 'ignore') as f:
        df = pd.read_csv(f)
    url_list = df.iloc[:,2].values
    #login_list=df.iloc[:,3].values
    print(url_list)
    #fname = "OutExchangeDataJapan.csv"
    fname="OutExchanges20181224.csv"
    fw = open(fname, 'w')
    fw.write("No,Exchange,URL,aliaslist,IP_Adder,Start,End,Serial,Algorithm,Issuer\n")
    for idx,p in enumerate(url_list):
        i=idx+1
        #i=idx+214
        sys.stdout.write("\r %d / %d" % (i, len(url_list)))
        sys.stdout.flush()
        fw.write("%d,%s,%s," % (i,df.iloc[idx,1],df.iloc[idx,2]))

        domain = p.split("//")[-1].split("/")[0]

        #login
        #pp=df.iloc[idx,3]
        #domain2=pp.split("//")[-1].split("/")[0]

        try:
            ip_adders = socket.gethostbyname_ex(domain)
            #ip_adders2 = socket.gethostbyname_ex(domain2)
            flag = True
        except:
            ip_adder = "error"
            flag = False

        #fw.write("%s," % (ip_adder))
        a="-"
        if(flag):
            try:
                for idx2,ip_ad in enumerate(ip_adders[2]):
                    if idx2==0:
                        fw.write("%s,%s," % (ip_adders[0],ip_ad))
                    else:
                        fw.write("%s,%s,%s,%s,%s," % (i,a,df.iloc[idx,2],ip_adders[0],ip_ad))
                    #
                    cert = ssl.get_server_certificate((ip_ad, 443))
                    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
                        # Following
                        # https://pyopenssl.org/en/stable/api/crypto.html

                    cert_serial = x509.get_serial_number()
                    cert_start  = x509.get_notBefore().decode('utf-8')
                    cert_end    = x509.get_notAfter().decode('utf-8')
                    cert_algo   = x509.get_signature_algorithm().decode('utf-8')
                    cert_issuer = x509.get_issuer().commonName

                    record = reader.city(ip_ad)

                    #isp=giisp.org_by_name(ip_ad)
                    asn=giasn.org_by_name(ip_ad)
                    asnum=re.match(r'AS\d+', asn)
                    ascom=re.split(r'^ ',re.split(r'AS\d+',asn)[1])[1]

                        #iss_components = x509.get_issuer().get_components()
                        #sub_components = x509.get_subject().get_components()
                    fw.write("%s,%s,%s,%s,%s,%s,%s,%s\n" % (cert_start,cert_end,str(cert_serial),cert_algo,cert_issuer,record.country.name,asnum.group(),ascom))
            #ssl._create_default_https_context = ssl._create_unverified_contt
            except:
                fw.write("error,error,error,error,error\n")
    else:
        fw.write("error,error,error,error,error,error,error\n")
    fw.close()

import pandas as pd
import socket
import sys
import ssl
import OpenSSL
import pyasn1

domain=["de908tco66xxm.cloudfront.net","hitbtc.com","bitbank.cc",
"d1rvkr24q4k2el.cloudfront.net","www.ethfinex.com","d1mjxfju5v8o21.cloudfront.net",
"simex.global","www.chaoex.com",
"btc-alpha.com","www.oex.com","www.bitcointrade.com.br",
"oasisdex.com","www.southxchange.com","www.iripplechina.com",
"stellarport.io","stellarterm.com","mydicewallet.com",
"exchange.dgtmarket.com","ddex.io","localtrade.pro",
"ore.bz","guldentrader.com","www.bitholic.com",
"www.barterdex.com","excambiorex.com","leoxchange.com",
"omniexplorer.info","dejff.x.incapdns.net","bitx.co",
"indacoin.com","hitbtc.com","www.gemini.com",
"de908tco66xxm.cloudfront.net","www.abucoins.com"
]
print(ssl.OPENSSL_VERSION)
print(len(domain))
ind=11 #chaoex 13irriple 23barterdex 24excambirex
#(ind=27)dejff.x.incapdns.net ssl.SSLError: [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:777)

print(domain[ind])
cert = ssl.get_server_certificate((domain[ind], 443),ssl_version=ssl.PROTOCOL_SSLv23)

x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
cert_serial = x509.get_serial_number()
cert_start  = x509.get_notBefore().decode('utf-8')
cert_end    = x509.get_notAfter().decode('utf-8')
cert_algo   = x509.get_signature_algorithm().decode('utf-8')
cert_issuer = x509.get_issuer().commonName
print("%s,%s,%s,%s,%s\n" % (cert_start,cert_end,str(cert_serial),cert_algo,cert_issuer))

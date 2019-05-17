import geoip2.database
import pandas as pd
import socket

# データベースの読み込み
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

inputname="url20181212.csv"
df = pd.read_csv(inputname)
ip_list = df.iloc[:,4].values
print(ip_list)
#fname = "OutCountryData8.csv"
fname = "OutCountryData8-url.csv"
fw = open(fname, 'w')
fw.write("No,Exchange,URL,aliaslist,IP_Adder,Start,End,Serial,Algorithm,Issuer,Country\n")

strerr="error"

for idx,p in enumerate(ip_list):
    idx=idx
    print("\r %d / %d" % (idx, len(ip_list)-1))

    #fw.write("%d,%s,%s,%s,%s,%s,%s,%s,%s,," % (df.iloc[idx,0],df.iloc[idx,1],df.iloc[idx,2],df.iloc[idx,3],df.iloc[idx,4],df.iloc[idx,5],df.iloc[idx,6],df.iloc[idx,7],df.iloc[idx,8],df.iloc[idx,9]))

    #fw.write("%s,%s,%s,%s,%s,%s,%s,%s,%s," % (df.iloc[idx,0],df.iloc[idx,1],df.iloc[idx,2],df.iloc[idx,3],df.iloc[idx,4],df.iloc[idx,5],df.iloc[idx,6],df.iloc[idx,7],df.iloc[idx,8]))
    fw.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," % (df.iloc[idx,0],df.iloc[idx,1],df.iloc[idx,2],df.iloc[idx,3],df.iloc[idx,4],df.iloc[idx,5],df.iloc[idx,6],df.iloc[idx,7],df.iloc[idx,8],df.iloc[idx,9]))

    if ip_list[idx]!="error" and ip_list[idx]!="\xe4":
        record = reader.city(ip_list[idx])
        """if "\xe4" in record.subdivisions.most_specific.name:
            record.subdivisions.most_specific.name.replace('\xe4', '')
        if "\xe4" in record.city.name:
            record.city.name.replace('\xe4', '')
        """
        fw.write("%s\n" % (record.country.name))
        #fw.write("%s,%s,%s\n" % (record.country.name,record.subdivisions.most_specific.name,record.city.name))
    else:
        fw.write("%s\n" %(strerr))

fw.close()

print("complete")

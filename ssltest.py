# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
import codecs
import time
import io
import re
import socket
from bs4 import BeautifulSoup
import sys
from selenium.common.exceptions import TimeoutException
from datetime import datetime

if(__name__ == "__main__"):
    #inputname="url20181224.csv"
    #df = pd.read_csv(inputname,header=None)
    #url_list = df.iloc[:,2].values
    inputname="domestic-bank2.csv"
    df = pd.read_csv(inputname,encoding="utf-8")
    url_list = df.iloc[:,4].values
    print(url_list)

    time=datetime.now()
    year=time.strftime('%Y%m%d%H%M')
    fname = "Bank-SslTest"+year+".csv"
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    #fw=pd.to_csv(fname,encoding="utf-8")
    fw = open(fname, 'w',encoding='utf-8')
    # ブラウザを開く。
    driver = webdriver.Chrome()
    RETRIES = 2
    TIMEOUT = 700
    driver.set_page_load_timeout(TIMEOUT)
    ssltesturl="https://www.ssllabs.com/ssltest/"

    for i in range(100,123):
        j = 0
        while j < RETRIES:
            try:
                driver.get(ssltesturl)
                search_box = driver.find_element_by_name("d")
                search_box.send_keys(url_list[i])
                search_box.submit()
                # 5秒間待機してみる。
                sleep(5)
                #sleep(400)
                ip_size=driver.find_elements_by_class_name('ip')

                a1=driver.find_elements_by_class_name("percentage_g")
                a2=driver.find_elements_by_class_name("percentage_a")
                a3=driver.find_elements_by_class_name("percentage_r")
                b1=driver.find_elements_by_class_name("rating_g")
                b2=driver.find_elements_by_class_name("rating_a")
                b3=driver.find_elements_by_class_name("rating_r")
                err=driver.find_elements_by_class_name("grayText")
                c=0
                loop=True
                while True:
                    if(len(a1)==len(ip_size) or len(a2)==len(ip_size) or len(a3)==len(ip_size) or len(b1)!=0 or len(b2)!=0 or len(b3)!=0 or c>10):
                        loop=False
                        print("break")
                        break
                    sleep(30)
                    print("sleep:%(c)s" %{'c':c})
                    c=c+1
                    a1=driver.find_elements_by_class_name("percentage_g")
                    a2=driver.find_elements_by_class_name("percentage_a")
                    a3=driver.find_elements_by_class_name("percentage_r")
                    b1=driver.find_elements_by_class_name("rating_g")
                    b2=driver.find_elements_by_class_name("rating_a")
                    b3=driver.find_elements_by_class_name("rating_r")
                    war=driver.find_elements_by_css_selector(".warningBox")

                #driver.save_screenshot('./out_img/Bank-search_results%(i)s.png' % {'i':i})
                ip_size=driver.find_elements_by_class_name('ip')

                html=driver.page_source
                #fw_html = codecs.open('./out_html/Bank-search_results%(i)s.html' % {'i':i}, 'w', "utf-8")
                #fw_html.write(str(html))
                a1=driver.find_elements_by_class_name("percentage_g")
                a2=driver.find_elements_by_class_name("percentage_a")
                a3=driver.find_elements_by_class_name("percentage_r")
                b1=driver.find_elements_by_class_name("rating_g")
                b2=driver.find_elements_by_class_name("rating_a")
                b3=driver.find_elements_by_class_name("rating_r")
                war=driver.find_elements_by_css_selector(".warningBox")
                print(war)
                print(len(war))
                fw = open(fname, 'a',encoding="utf-8")
                fw.write("%d,%s," % (i,url_list[i]))
                if len(a1)!=0:
                    for j in range(0,len(a1)):
                        print(a1[j].text)
                        fw.write("%s," % (a1[j].text))
                elif(len(a2)!=0):
                    for j in range(0,len(a2)):
                        print(a2[j].text)
                        fw.write("%s," % (a2[j].text))
                elif(len(a3)!=0):
                    for j in range(0,len(a3)):
                        print(a3[j].text)
                        fw.write("%s," % (a3[j].text))
                elif(len(b1)!=0):
                    print(b1[0].text)
                    fw.write("%s," % (b1[0].text))
                elif(len(b2)!=0):
                    print(b2[0].text)
                    fw.write("%s," % (b2[0].text))
                elif(len(b3)!=0):
                    print(b3[0].text)
                    fw.write("%s," % (b3[0].text))
                if(len(war)!=0):
                    fw.write(",,")
                    for j in range(0,len(war)):
                        print(war[j].text)
                        #war[j].text.replace(',', ' ')
                        new_text = re.sub(r',', " ", war[j].text)
                        fw.write("%s," % (new_text))
                fw.write("\n")

                soup = BeautifulSoup(html, 'lxml')
                tables = soup.findAll('table', id='multiTable')
                for table in tables:
                    for z,tr in enumerate(table.findAll('tr')):
                        for link in tr.find_all('a'):
                            rel_link=link.get('href')
                            if rel_link!='':
                                driver.execute_script("window.open()")
                                new_window = driver.window_handles
                                driver.switch_to.window(new_window[-1])
                                print(rel_link)
                                driver.get(ssltesturl+rel_link)
                                sleep(3)
                                html2=driver.page_source
                                #fw_html = codecs.open('./out_html/Bank-search_results%(i)s-%(z)s.html' % {'i':i,'z':z}, 'w', "utf-8")
                                #fw_html.write(str(html2))
                                #driver.save_screenshot('./out_img/Bank-search_results%(i)s-%(z)s.png' % {'i':i,'z':z})


                driver.execute_script("window.open()")
                new_window = driver.window_handles
                driver.switch_to.window(new_window[-1])
                print(i)
                fw.close()
                break
            except TimeoutException:
                j = j + 1
                print("Timeout, Retrying... (%(i)s %(j)s/%(max)s)" % {'i':i,'j': j, 'max': RETRIES})
                if(j>RETRIES):
                    i=i+1
                    break
                continue
            else:
                print("error (%i)s" % {'i':i})
                break
# ブラウザを終了する。
#driver.close()

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas as pd
import codecs
import time
import socket
from bs4 import BeautifulSoup
import sys
from selenium.common.exceptions import TimeoutException
from datetime import datetime

if(__name__ == "__main__"):
    inputname="domestic-bank2.csv"
    df = pd.read_csv(inputname)
    url_list = df.iloc[:,4].values
    print(url_list)

    # ブラウザを開く。
    driver = webdriver.Chrome()
    RETRIES = 2
    TIMEOUT = 700
    driver.set_page_load_timeout(TIMEOUT)
    ssltesturl="https://www.ssllabs.com/ssltest/"

    for i in range(105,123):
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
                """
                html=driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                #soup = BeautifulSoup(html,"html.parser")

                tables = soup.findAll('table', id='multiTable')

                for table in tables:
                    for tr in table.findAll('tr'):
                        for link in tr.find_all('a'):
                            rel_link=link.get('href')
                            if rel_link!='':
                                driver.execute_script("window.open()")
                                new_window = driver.window_handles
                                driver.switch_to.window(new_window[-1])
                                print(rel_link)
                                driver.get(ssltesturl+rel_link)
                """
                driver.execute_script("window.open()")
                new_window = driver.window_handles
                driver.switch_to.window(new_window[-1])
                print(i)
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

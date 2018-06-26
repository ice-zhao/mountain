#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# html = urlopen("http://fund.eastmoney.com/f10/jjjz_501018.html")    #QDII-FOF
# bsobj = BeautifulSoup(html.read(), "lxml")
# print(bsobj)
# exit(0)
# print(bsobj.div)
# namelist = bsobj.find(text="历史净值明细")
# print(namelist)

# driver = webdriver.PhantomJS(executable_path='/usr/bin/phantomjs')
# driver = webdriver.FireFox(firefox_profile=getProfile())
driver = webdriver.firefox.webdriver.WebDriver(firefox_binary='/usr/bin/firefox')
# driver = webdriver.FireFox()
driver.get("http://fund.eastmoney.com/f10/jjjz_501018.html")
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(5)
# print(driver.find_element_by_id("content").text)
# pageSource = driver.page_source
# bsobj = BeautifulSoup(pageSource, 'lxml')
# print(bsobj)
# exit(0)
# time.sleep(1)
# print(driver.find_elements_by_id('jztable'))
# for item in bsobj.find('div', {'id':'jztable'}):
# for item in bsobj.find('table', {'class':['w782', 'comm', 'lsjz']}).tbody.tr.next_siblings:
# for item in bsobj.find('label', {'value':'3'}):
    # print(item)
    # if re.match(item.get_text(), 'value="3"'):
        # print(item)
# print(driver.find_element(By.XPATH, "//*[@class=pagebtns]"))
# driver.find_element(By.CLASS_NAME, "end").click()
# print(driver.find_element(By.CLASS_NAME, "end").text)
# i=0
# for page in driver.find_element(By.CLASS_NAME, "pagebtns"):
#     if i < 3:
#         i=i+1
#         continue
#     page.click()
#     break
for idx in range(1,15):
    driver.find_element(By.CLASS_NAME, "pnum").send_keys(str(idx))
    driver.find_element(By.CLASS_NAME, "pnum").send_keys(Keys.RETURN)
    driver.find_element(By.CLASS_NAME, "pgo").click()
# time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lsjz")))
    pageSource = driver.page_source
    bsobj = BeautifulSoup(pageSource, 'lxml')
    # print(item.get_text())
    # if item.get_text().find('下一页') != -1:    #find item
        # print(item.attrs)
        # item.click()
        # break
# print(bsobj)
# exit(0)

    date = ''
    netvalue = ''
    rate = 0
    for item in bsobj.find('table', {'class':['w782', 'comm', 'lsjz']}).tbody.children:
    # print(item.attrs)
    # print(item)
        bstr = BeautifulSoup(str(item), 'html.parser')
        trlist = bstr.findAll('td')
        date = trlist[0].get_text()
        netvalue = trlist[1].get_text()
        rate = trlist[3].get_text()

        print("%s, %s, %s" % (date, netvalue, rate))
    # for i in bstr.findAll('td'):
        # print(i)
driver.close()
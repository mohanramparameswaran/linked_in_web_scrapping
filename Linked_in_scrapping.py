# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:05:45 2020

@author: mohan
"""


import os,random,sys,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import re

browser = webdriver.Chrome('D:\Studies\python\LINKED_IN\chromedriver_win32\chromedriver.exe')


browser.get('https://www.linkedin.com/uas/login')

os.chdir(r'D:\Studies\python\LINKED_IN')
file = open('profile.txt')
lines = file.readlines()

username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)


elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

visitingProfileID = '/company/accenture/mycompany/verification/'
fullLink = 'https://www.linkedin.com/' + visitingProfileID

browser.get(fullLink)

#browser.find_element_by_xpath('//div[@class="msg-overlay-list-bubble"]/*[name()="svg"][@aria-label="Search"]').click()


browser.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221033%22%2C%22217062%22%2C%22456960%22%2C%22336238%22%2C%222936833%22%2C%2248925%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH")


time.sleep(20)
"""
url = "https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221033%22%2C%22217062%22%2C%22456960%22%2C%22336238%22%2C%222936833%22%2C%2248925%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH"

req = requests.get(url)



con = req.content
soup = BeautifulSoup(con, "html.parser")
#print(soup.prettify())
#content = soup.find_all('div', {'class', 'authentication-outlet'})
#print(content)
mydivs = soup.find("section", {"id": "artdeco-toasts"})

content = str(mydivs)

print(content[:10])

"""
page_source=browser.page_source

soup = BeautifulSoup(page_source,'lxml')

span_list=soup.find_all('span',{'class', 'name actor-name'})



"""
for i in range (2,5):
    browser.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221033%22%2C%22217062%22%2C%22456960%22%2C%22336238%22%2C%222936833%22%2C%2248925%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page="+str(i))
    page_source=browser.page_source

    soup = BeautifulSoup(page_source,'lxml')
    
    span_list.append(soup.find_all('span',{'class', 'name actor-name'}))
    
"""
    
#print(span_list)

print(type(span_list[0]))


result_array=[]

for i in span_list:
    result = re.search('<span class="name actor-name">(.*)</span>', str(i))
    result_array.append(result.group(1))
    
print(result_array)

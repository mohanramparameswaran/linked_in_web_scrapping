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
import pandas as pd
import re


browser = webdriver.Chrome(r'C:\Users\mohan.r.parameswaran\.spyder-py3\chromedriver_win32\chromedriver.exe')


browser.get('https://www.linkedin.com/uas/login')

os.chdir(r'C:\Users\mohan.r.parameswaran\.spyder-py3')
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

time.sleep(2)
browser.execute_script("window.scrollTo(0, 800)") 
time.sleep(2)
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

p_list=soup.find_all('p',{'class', 'subline-level-1 t-14 t-black t-normal search-result__truncate'})


result_array=[]
result_array1=[]

for i in span_list:
    result = re.search('<span class="name actor-name">(.*)</span>', str(i))
    result_array.append(result.group(1))
    
for i in p_list:
    j=str(i)
    result_array1.append(j[82:-9])

for i in range (2,5):
    browser.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221033%22%2C%22217062%22%2C%22456960%22%2C%22336238%22%2C%222936833%22%2C%2248925%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page="+str(i))
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, 800)") 
    time.sleep(2)
    page_source=browser.page_source
    soup = BeautifulSoup(page_source,'lxml')
    
    span_list1=soup.find_all('span',{'class', 'name actor-name'})
    for i in span_list1:
        result = re.search('<span class="name actor-name">(.*)</span>', str(i))
        result_array.append(result.group(1))
    
    p_list=soup.find_all('p',{'class', 'subline-level-1 t-14 t-black t-normal search-result__truncate'})
    for i in p_list:
        j=str(i)
        result_array1.append(j[82:-9])
    
        
    
    

    
#print(span_list)



print("-----------names------")
    
print(result_array)

print("------role---------")
print(result_array1)



print('---------------names count---------')
print(len(result_array))


print('---------------roles count---------')
print(len(result_array1))



dic={"Names":result_array,"Role":result_array1}
df=pd.DataFrame(dic)
df.to_excel(r"C:\Users\mohan.r.parameswaran\1.my_folder\python\Linked_in_scrap.xlsx")



browser.quit()

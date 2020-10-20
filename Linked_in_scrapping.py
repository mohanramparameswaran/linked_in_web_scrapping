# -*- coding: utf-8 -*-
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

visitingProfileID = '/company/accenture'
fullLink = 'https://www.linkedin.com/' + visitingProfileID

browser.get(fullLink)

time.sleep(2)

page_source=browser.page_source

soup = BeautifulSoup(page_source,'lxml')

link = soup.find_all('a',{'class', 'ember-view link-without-visited-state inline-block'})

link_str=str(link)
a=link_str.split('href="')
b=a[1]
c=b.split('"')
emp_link = c[0]

emp_details_link= 'https://www.linkedin.com' + str(emp_link)

browser.get(emp_details_link)

time.sleep(2)
browser.execute_script("window.scrollTo(0, 800)") 
time.sleep(2)

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
    browser.get(emp_details_link+"&page="+str(i))
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

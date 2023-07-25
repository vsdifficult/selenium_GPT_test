from bs4 import BeautifulSoup 
from selenium import webdriver

import pandas as pd
import  requests 


driver = webdriver.Chrome('./chromedriver.exe') 

driver.close()

response = requests.get('http://free-proxy.cz/ru/')
data = pd.read_html(response.text) 
print(data) 

with open('proxi.txt','w', encoding='utf-16') as f: 
     f.write(str(data)) 

bs4  = BeautifulSoup(response.text, 'html.parser') 
print(bs4) 

with open('proxi_.txt', 'w', encoding='utf-8') as f: 
     f.write(str(f))

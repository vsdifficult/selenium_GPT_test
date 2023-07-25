from selenium import webdriver 
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup 

import requests as r


def driver_optios(page,s,  arg1): 
                
                driver = webdriver.Chrome('./chromedriver.exe') 
                driver.get(page) 
                search = driver.find_element(By.CLASS_NAME, arg1) 
                search.send_keys(s)
    
                for result in search: 
                   print(result) 
             
                driver.close() 
                response = r.get(page) 
                bs4obj = BeautifulSoup(response.text, 'html.parser' )  

                for element in arg1: 
                    if bs4obj.find(arg1): 
                        print(element)


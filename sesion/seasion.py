

from selenium import webdriver 
from selenium.webdriver.common.by import By


def main_parser_funciotn(message, element1, element2): 
    driver = webdriver.Chrome('./chromedriver.exe') 
    driver.get("https://www.google.com")
    serach = driver.find_element(By.CLASS_NAME, element1) 

    serach.send_keys(message) 
    serach.submit() 

    serach_result = driver.find_elements(element2)
     
    for result in serach_result: 
        with open('res.txt', 'w', encoding='utf-8') as f: 
            f.write(str(result))

        driver.close() 

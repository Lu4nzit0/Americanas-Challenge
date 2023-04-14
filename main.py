from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import csv

# os.system("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome()
driver.implicitly_wait(30)

def openAmericanasSite():
    driver.get("https://www.americanas.com.br/")


def searchIphone():
    driver.find_element(By.XPATH, ("//input[@aria-label='Pesquisar']")).send_keys("iphone")
    driver.find_element(By.XPATH, ("//button[@aria-label='pesquisar']")).click()

def returnTitles():
   titles = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/h3[contains(@class,'gUjFDF')]"))
   return titles

def returnPrices():
    prices = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/span[contains(@class,'liXDNM')]"))
    return prices

openAmericanasSite()
searchIphone()
titles = returnTitles()
prices = returnPrices()

for title in titles:
    print(title.text)
    
for price in prices:
    print(price.text)

# findProductInformation()

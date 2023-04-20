from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import csv

os.system("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome()
driver.implicitly_wait(30)

def open_americanas_site():
    driver.get("https://www.americanas.com.br/")


def search_iphone():
    driver.find_element(By.XPATH, ("//input[@aria-label='Pesquisar']")).send_keys("iphone")
    driver.find_element(By.XPATH, ("//button[@aria-label='pesquisar']")).click()

open_americanas_site()
search_iphone()

titles = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/h3[contains(@class,'gUjFDF')]"))

def return_titles(position):   
   return titles[position].text

prices = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/span[contains(@class,'liXDNM')]"))
def return_prices(position):    
    return prices[position].text

index = 0

while(index <= 23):
   print("Título: " + return_titles(index))
   print("Preco: " + return_prices(index))
   print()
   index = index + 1

   





# findProductInformation()

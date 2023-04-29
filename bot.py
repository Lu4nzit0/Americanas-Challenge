from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os

os.system("TASKKILL /f /IM CHROME.EXE")

driver = webdriver.Chrome()
driver.implicitly_wait(30)

def open_americanas_site():
    driver.get("https://www.americanas.com.br/")


def search_product():
    product = str(input('Digite o nome produto: '))
    driver.find_element(By.XPATH, ("//input[@aria-label='Pesquisar']")).send_keys(product)
    driver.find_element(By.XPATH, ("//button[@aria-label='pesquisar']")).click()

open_americanas_site()
search_product()

title_element = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/h3[contains(@class,'gUjFDF')]"))

def return_title_element(position):
    title = title_element[position].text
    titles.append(title)
    return title

price_element = driver.find_elements(By.XPATH, ("//a[contains(@class,'inStockCard')]//div/span[contains(@class,'liXDNM')]"))

def return_price_element(position): 
    price = price_element[position].text
    prices.append(price)
    return price

prices = []
titles = []

index = 0

while(index < len(title_element)):
   print("Título: " + return_title_element(index))
   print("Preco: " + return_price_element(index))
   print()
   index = index + 1 

products = pd.DataFrame({'Titulo': titles, 'Preco': prices})

print(products)

products.to_excel('resultado.xlsx')

driver.quit()

print('\n''Relatório gerado com sucesso!')

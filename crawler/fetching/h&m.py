from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json


tit , pri , imgref , prodlink= [] , [] , [] , []

ProductsArr = None
s=Service(ChromeDriverManager().install())
options = Options()
options.headless = True
driver = webdriver.Chrome(service=s , options=options)
searchedProduct = "jacket"
url = "https://eg.hm.com/en/#query=" + searchedProduct
driver.get(url)

products = driver.find_elements(By.CLASS_NAME , "c-products__item") 

for product in products: 
    title = product.find_element(By.CLASS_NAME, "field--name-name").text
    price = product.find_element(By.CLASS_NAME, "price").text
    img = product.find_element(By.TAG_NAME , "img").get_attribute('src')
    link = product.find_element(By.TAG_NAME , "a").get_attribute("href")

    tit.append(title)
    pri.append(price)
    imgref.append(img)
    prodlink.append(link)   

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
print(ProductsArr)     

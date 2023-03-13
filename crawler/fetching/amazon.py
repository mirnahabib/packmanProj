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
searchedProduct = "playstation 5"
url = "https://www.amazon.eg/-/en/s?k=" + searchedProduct
driver.get(url)

products = driver.find_elements(By.CLASS_NAME,"a-spacing-base")

for product in products[:20]:
    title = product.find_element(By.CLASS_NAME, "a-size-mini").text
    try:
        price = product.find_element(By.CLASS_NAME , "a-price-whole").text
    except:
          price = None
    link = product.find_element(By.CLASS_NAME , "s-product-image-container").find_element(By.TAG_NAME, "a").get_attribute("href")
    img =  product.find_element(By.CLASS_NAME , "s-product-image-container").find_element(By.TAG_NAME, "img").get_attribute("src")       
    
    tit.append(title)
    pri.append(price)
    imgref.append(img)
    prodlink.append(link)

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

print(ProductsArr)

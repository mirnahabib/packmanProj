from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json


tit , pri , imgref , prodlink= [] , [] , [] , []

ProductsArr = None
s=Service(ChromeDriverManager().install())
options = Options()
options.headless = False
driver = webdriver.Chrome(service=s , options=options)
searchedProduct = "jeans"
url = "https://www.zara.com/eg/en/search?searchTerm=" + searchedProduct
driver.get(url)
driver.implicitly_wait(3)

products = driver.find_elements(By.CLASS_NAME , "product-grid-product")

for product in products:
    ActionChains(driver).scroll_to_element(product).perform()
    title = product.find_element(By.CLASS_NAME , "product-grid-product-info__name")
    price = product.find_element(By.CLASS_NAME, "money-amount__main")
    link = title.get_attribute("href")
    img = product.find_element(By.CLASS_NAME, "media-image__image").get_attribute("src")

    tit.append(title.text)
    pri.append(price.text)
    imgref.append(img)
    prodlink.append(link)


ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
print(ProductsArr)

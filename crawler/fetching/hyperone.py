from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json , time


tit , pri , imgref , prodlink= [] , [] , [] , []


ProductsArr = None
s=Service(ChromeDriverManager().install())
options = Options()
options.headless = True
driver = webdriver.Chrome(service=s , options=options)
searchedProduct = "corn flakes"
url = "https://www.hyperone.com.eg/search?q=" + searchedProduct
driver.get(url)
driver.implicitly_wait(10)

products = driver.find_elements(By.CLASS_NAME , "ProductCard")

for product in products:
    title = product.find_element(By.CLASS_NAME , "ProductTitle").text
    price = product.find_element(By.XPATH , "./div[2]/a/div/div[1]").text
    link = product.find_element(By.TAG_NAME , "a").get_attribute("href")
    img = product.find_element(By.TAG_NAME , "img").get_attribute("src")

    tit.append(title)
    pri.append(price)
    imgref.append(img)
    prodlink.append(link)

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

print(ProductsArr)

    

    
# //*[@id="main"]/div/div[1]/div/div/div[3]/article[1]
# //*[@id="main"]/div/div[1]/div/div/div[3]/article[1]


# //*[@id="main"]/div/div[1]/div/div/div[3]/article[4]
# //*[@id="main"]/div/div[1]/div/div/div[3]/article[4]/div[2]/a/div/div[1]
# 
# //*[@id="main"]/div/div[1]/div/div/div[3]/article[4]/div[2]/a/div/div[2]
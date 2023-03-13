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

searchedProduct = "playstation"
url = "https://www.jumia.com.eg/catalog/?q=" + searchedProduct
driver.get(url)

popup = driver.find_element(By.CLASS_NAME,"cw")
close = popup.find_element(By.XPATH,"./button").click()


products = driver.find_elements(By.CLASS_NAME,"c-prd")

for product in products:
        title = product.find_element(By.CLASS_NAME,"name")
        price = product.find_element(By.CLASS_NAME,"prc")
        link = product.find_element(By.CLASS_NAME,"core").get_attribute("href")
        img = product.find_element(By.XPATH,"./a/div[1]/img").get_attribute("data-src")
        
        tit.append(title.text)
        pri.append(price.text)
        imgref.append(img)
        prodlink.append(link)

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
print(ProductsArr)
        






#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[5]
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[5]/a
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[5]/a/div[1]/img
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[5]/a/div[2]/h3
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[5]/a/div[2]/div[1]

#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[49]/a/div[2]/div[2]


#popup
# //*[@id="pop"]/div/section
#//*[@id="pop"]/div/section/button

#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[49]
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[49]/a/div[1]/img
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[49]/a/div[2]/h3
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[49]/a/div[2]/div[2]
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[45]/a/div[2]/div[1]
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[20]/a/div[2]/div[1]
#//*[@id="jm"]/main/div[2]/div[3]/section/div[1]/article[44]/a/div[2]/div[1]
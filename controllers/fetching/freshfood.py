
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


tit , pri , imgref= [] , [] , []


ProductsArr = None
PATH = "D:\est\chromedriver_win32_3new\chromedriver.exe"
driver = webdriver.Chrome(PATH)
searchedProduct = "milk"
url = "https://new.freshfood-market.com/search?key=" + searchedProduct
driver.get(url)
driver.implicitly_wait(3)


for i in range(1,7):
    tittle = driver.find_element(By.XPATH,f'//*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[{i}]/div/div/div[2]/p[1]')
    price = driver.find_element(By.XPATH,f"//*[@id='__next']/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[{i}]/div/div/p/a[1]")
    img = driver.find_element(By.XPATH,f"//*[@id='__next']/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[{i}]/div/div/div[1]/div/img")
    imgURL = img.get_attribute('src')
    print (tittle.text, ' ' , price.text , ' ' , imgURL)
    


#prices
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[16]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[4]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[5]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[6]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[7]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/p/a[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/p/a[1]



# whole product 
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[6]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[13]
# 

# titles
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/p[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]/p[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/p[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[19]/div/div/div[2]/p[1]
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[11]/div/div/div[2]/p[1]


#img 
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div[1]/div/img
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div[1]/div/img
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]/div/div/div[1]/div/img
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[4]/div/div/div[1]/div/img
# //*[@id="__next"]/div[3]/div/main/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[16]/div/div/div[1]/div/img
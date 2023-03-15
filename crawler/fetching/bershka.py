from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json,time


tit , pri , imgref , prodlink= [] , [] , [] , []

ProductsArr = None
s=Service(ChromeDriverManager().install())
options = Options()
options.headless = False
driver = webdriver.Chrome(service=s , options=options)
driver.maximize_window()
searchedProduct = "jacket"
url = "https://www.bershka.com/eg/en/q/" + searchedProduct
driver.get(url)
driver.implicitly_wait(15)

# gender = driver.find_element(By.CLASS_NAME, "gender-filters")
# men = gender.find_element(By.XPATH , "./button[3]").click()
# women = gender.find_element(By.XPATH , "./button[2]")

products = driver.find_elements(By.CLASS_NAME , "search-product-card")


for product in products[1:]:
    ActionChains(driver).scroll_to_element(product).perform()
    title = product.find_element(By.CLASS_NAME , "product-text").text
    price = product.find_element(By.CLASS_NAME, "current-price-elem").text
    img = product.find_element(By.CLASS_NAME , "image-item").get_attribute("src")
    link = product.find_element(By.CLASS_NAME , "grid-card-link").get_attribute("href")

    tit.append(title)
    pri.append(price)
    imgref.append(img)
    prodlink.append(link)

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

print(ProductsArr)




# //*[@id="main-content"]/div/div[1]/div/div
# //*[@id="main-content"]/div/div[1]/div/div/button[2]
# //*[@id="main-content"]/div/div[1]/div/div/button[3]
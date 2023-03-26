from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json , time , sys


def main(searchitem):

    tit , pri , imgref , prodlink= [] , [] , [] , []


    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = searchitem
    url = "https://select.eg/en/pages/search-results-page?q=" + searchedProduct
    driver.get(url)
    driver.implicitly_wait(10)


    products = driver.find_elements(By.CLASS_NAME , "snize-product-in-stock")

    for product in products:
        title = product.find_element(By.CLASS_NAME , "snize-title").text
        price = product.find_element(By.CLASS_NAME , "snize-price").text
        link = product.find_element(By.CLASS_NAME, "snize-view-link").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "snize-item-image").get_attribute("src")

        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link) 

    ProductsArr = [{ "Shop":"Select" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)
    
if __name__ == "__main__":
    main(sys.argv[1])
            
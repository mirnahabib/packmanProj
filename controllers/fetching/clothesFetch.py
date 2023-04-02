from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask import Flask , jsonify , request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
import json,sys

def bershka(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = query
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

    ProductsArr = [{ "Shop":"Bershka" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

    print(ProductsArr)

def zara(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
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


    ProductsArr = [{ "Shop":"Zara" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

def max(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = query
    url = "https://www.maxfashion.com/eg/en/search?q=" + searchedProduct
    driver.get(url)

    # body = driver.find_element(By.TAG_NAME , "body")
    # body.click
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    # time.sleep(1)
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()



    products = driver.find_elements(By.CLASS_NAME , "product")


    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.XPATH , './div[3]')
        price = product.find_element(By.XPATH , './div[2]')
        img_link = product.find_element(By.XPATH , "./div[1]")
        link = img_link.find_element(By.TAG_NAME , "a").get_attribute("href")
        imgs = img_link.find_elements(By.TAG_NAME , "img")
        img= imgs[1].get_attribute("src")
    
        
        tit.append(title.text)
        pri.append(price.text)
        imgref.append(img)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Max" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

def handm(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
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

    ProductsArr = [{ "Shop":"H&M" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)  

#TODO: Optmize code, join all results, test multiple word parameters

def main(query):
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(zara, query)  
        future2 = executor.submit(handm, query)  
        future3 = executor.submit(max, query)  
        future4 = executor.submit(bershka, query)  


if __name__ == "__main__":
    main(sys.argv[1])

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

def hyperone(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []
    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
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

    ProductsArr = [{ "Shop":"Hyperone" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

    print(ProductsArr)

def gourmet(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []


    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
    url = "https://gourmetegypt.com/catalogsearch/result/?q=" + searchedProduct
    driver.get(url)
    driver.implicitly_wait(3)
    allProducts = driver.find_element(By.CLASS_NAME, "products-group")
    products = allProducts.find_elements(By.CLASS_NAME , "product-item-info")

    for product in products:
        title = product.find_element(By.CLASS_NAME , "product-item-link").get_attribute("innerHTML")
        price = product.find_element(By.CLASS_NAME , "price").get_attribute("innerHTML")
        link = product.find_element(By.CLASS_NAME , "product-item-photo").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "product-image-photo").get_attribute("src")

        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Gourmet" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

    print(ProductsArr)

def spinney(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = query
    url = "https://spinneys-egypt.com/en/search?term=" + searchedProduct
    driver.get(url)


    products = driver.find_elements(By.CLASS_NAME , "sp-product")
    # driver.implicitly_wait(3)
    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "text-capitalize").text
        price = product.find_element(By.CLASS_NAME , "priceAfter").text
        link = product.find_element(By.CLASS_NAME , "imgwrap").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "lazy").get_attribute("src")
        
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Spinney" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

def carrefour(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []
    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
    url = "https://www.carrefouregypt.com/mafegy/en/v4/search?keyword=" + searchedProduct
    driver.get(url)


    products = driver.find_elements(By.CLASS_NAME , "css-b9nx4o")

    for product in products: 
        title = product.find_element(By.CLASS_NAME , "css-1nhiovu")
        price = product.find_element(By.CLASS_NAME , "css-17fvam3").text
        link = title.find_element(By.XPATH , "./a").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "css-1itwyrf")
        pic = img.find_element(By.XPATH , "./a/img").get_attribute("src")
        
        tit.append(title.text)
        pri.append(price)
        imgref.append(pic)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Carrefour" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

def freshfood(query):
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

#Optmize code, join all results, test multiple word parameters

def main(query):
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(hyperone, query)  
        future2 = executor.submit(gourmet, query)  
        future3 = executor.submit(spinney, query)  
        future4 = executor.submit(carrefour, query)  


if __name__ == "__main__":
    main(sys.argv[1])

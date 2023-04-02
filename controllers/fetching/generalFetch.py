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
import time

def amazon(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []
    ProductsArr = None
    s=Service(ChromeDriverManager().install())

    prefs = {"profile.managed_default_content_settings.images": 2}
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload

    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
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

    ProductsArr = [{ "Shop":"Amazon" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]

    print(ProductsArr) 

def jumia(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []
    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=s , options=options)

    url = "https://www.jumia.com.eg/catalog/?q=" + query
    driver.get(url)

    popup = driver.find_element(By.CLASS_NAME,"cw")
    popup.find_element(By.XPATH,"./button").click()


    products = driver.find_elements(By.CLASS_NAME,"c-prd")

    for product in products[:20]:
            title = product.find_element(By.CLASS_NAME,"name")
            price = product.find_element(By.CLASS_NAME,"prc")
            link = product.find_element(By.CLASS_NAME,"core").get_attribute("href")
            img = product.find_element(By.XPATH,"./a/div[1]/img").get_attribute("data-src")
    
            tit.append(title.text)
            pri.append(price.text)
            imgref.append(img)
            prodlink.append(link)

    ProductsArr = [{ "Shop":"Jumia" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    
    print (ProductsArr)

def noon(query):
    tit , pri , imgref , productURL= [] , [] , [] , []
    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.noon.com/egypt-en/search/?q=" + query
    driver.get(url)
    driver.implicitly_wait(10)
    products = driver.find_elements(By.CLASS_NAME, "productContainer")

    for product in products[:20]:
        #ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "sc-5e50ccb9-20").get_attribute("title")
        price = product.find_element(By.CLASS_NAME , "sc-6073040e-1").text
        link = product.find_element(By.XPATH , "./a")
        linkURL= link.get_attribute("href")
        try:
            img = link.find_element(By.CLASS_NAME,"lazyload-wrapper").find_element(By.TAG_NAME, "img").get_attribute("src")
            
        except:
            img = None
               
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        productURL.append(linkURL) 

    ProductsArr = [{"Shop":"Noon", "Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,productURL)]
    print(ProductsArr)

def select(query):
    tit , pri , imgref , prodlink= [] , [] , [] , []


    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://select.eg/en/pages/search-results-page?q=" + query
    driver.get(url)
    driver.implicitly_wait(10)


    products = driver.find_elements(By.CLASS_NAME , "snize-product-in-stock")

    for product in products[:20]:
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

def olx(query):
    query = query.replace(" " , "-")

    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.olx.com.eg/en/ads/q-" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "_7e3920c1")

    for product in products[:20]:
        #ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "a5112ca8").text
        try:
            price = product.find_element(By.CLASS_NAME , "_95eae7db").text
        except:
            price = "Seller didn't add the price"    
        img = product.find_element(By.CLASS_NAME , "_76b7f29a").get_attribute("src")
        link = product.find_element(By.CLASS_NAME, "ee2b0479").find_element(By.TAG_NAME, "a").get_attribute("href")
        
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link) 

    ProductsArr = [{ "Shop":"OLX" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    x = json.dumps(ProductsArr)
    print(x)

#Optmize code, join all results, test multiple word parameters


def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(amazon, query)  
        future2 = executor.submit(jumia, query)  
        future3 = executor.submit(select, query)  
        future4 = executor.submit(olx, query)  
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main(sys.argv[1])

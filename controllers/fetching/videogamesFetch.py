from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
import json, sys, re

s = Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []



def games2egypt(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.games2egypt.com/Web/Products/Index?search=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product__item")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product__title")
        try:
            price = product.find_element(By.CLASS_NAME , "int_price").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            continue   
        img = product.find_element(By.CLASS_NAME , "product__img").find_element(By.TAG_NAME , "img").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        try :
            product.find_element(By.CLASS_NAME, "out_of_stock")
        except:
            ProductsArr.append({
                "Count" : i,
                "Shop"  : "Games2Egypt",
                "Title" : title,
                "Price" : float(price),
                "Link"  : link,
                "Img"   : img
            } )
            i += 1
    driver.close()

def egygamer(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://www.egygamer.com/en/catalogsearch/result/?q={query}"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"product-item")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "product-item-link")
        try:
            price = product.find_element(By.CLASS_NAME , "price").text
            price = re.sub(r"[^0-9\.]+" , '' , price)  
        except:
            continue

        link = title.get_attribute('href')
        img =  product.find_element(By.CLASS_NAME , "product-image-photo").get_attribute("src")  
        title = title.text.replace('"', "")
        try: 
            product.find_element(By.CLASS_NAME, "unavailable")
        except:    
            ProductsArr.append({
                "Count" : i,
                "Shop"  : "Egygamer",
                "Title" : title,
                "Price" : float(price),
                "Link"  : link,
                "Img"   : img
            })
            i += 1
    driver.close()

def shamy(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://shamystores.com/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=last&q=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product-item")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-item__title")
        try:
            price = product.find_element(By.CLASS_NAME , "price").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            price = 0    
        img = product.find_element(By.CLASS_NAME , "product-item__primary-image").get_attribute("srcset")
        link = title.get_attribute("href")
        title = title.text
        
        availability = product.find_element(By.CLASS_NAME, "product-item__inventory").text
        if availability == "Sold out":
            continue
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Shamy",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()

def gameworld(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.gamesworldegypt.com/index.php?route=product/search&search=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product-layout")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-title").text
        try:
            price = product.find_element(By.CLASS_NAME , "price-new").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            price = product.find_element(By.CLASS_NAME , "price").text    
            price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.CLASS_NAME , "image")
        link = img.find_element(By.TAG_NAME, "a").get_attribute("href")
        img = img.find_element(By.TAG_NAME, "img").get_attribute("src")
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Game World",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()        



def main(query):
    with ThreadPoolExecutor(max_workers=25) as executor:
    
        future = executor.submit(games2egypt, query)
        future = executor.submit(egygamer, query)  
        future = executor.submit(shamy, query) 
        future = executor.submit(gameworld, query)
    print(json.dumps(ProductsArr, ensure_ascii = True ))

if __name__ == "__main__":
    main(sys.argv[1])

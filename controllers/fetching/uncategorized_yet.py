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


def fabegypt(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://fabegypt.com/?s={query}&post_type=product"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"product")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "hongo-LoopProduct-link")
        try:
            price = product.find_element(By.CLASS_NAME , "price")
            price = price.find_element(By.TAG_NAME, "ins").text
        except:
            price = product.find_element(By.CLASS_NAME , "price").text
        price = re.sub(r"[^0-9\.]+" , '' , price)  
        link = title.get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "attachment-woocommerce_thumbnail").get_attribute("src")  
        title = title.text

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Fab Egypt",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()     

def egyptlaptop(query):
    i = 1    
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://egyptlaptop.com/?match=all&subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q={query}&dispatch=products.search"
    driver.get(url)
    driver.implicitly_wait(1)
    products = driver.find_element(By.ID,"products_search_pagination_contents")
    products = products.find_elements(By.CLASS_NAME, "ty-column4")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "product-title")
        try:
            price = product.find_element(By.CLASS_NAME , "ty-price-num").text
            price = re.sub(r"[^0-9\.]+" , '' , price)  
        except:
            price = 0
        
        link = title.get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "cm-image").get_attribute("src")  
        title = title.text

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Egypt Laptop",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()      

def bouri(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://bouri.com/catalogsearch/result/?q={query}"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"product-item-info")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "product-item-link")
        try:
            price = product.find_element(By.CLASS_NAME , "price").text
        except:
            price = 0
        price = re.sub(r"[^0-9\.]+" , '' , price)  
        link = title.get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "product-image-photo").get_attribute("src")  
        title = title.text

        try:
            product.find_element(By.CLASS_NAME, "unavailable")
        except:    
            ProductsArr.append({
                "Count" : i,
                "Shop"  : "Bouri",
                "Title" : title,
                "Price" : float(price),
                "Link"  : link,
                "Img"   : img
            })
            i += 1
    driver.close()      


def main(query):
    with ThreadPoolExecutor(max_workers=25) as executor:
        # future = executor.submit(egyptlaptop, query) # for laptops, for some reason site is down now xd

        future = executor.submit(fabegypt, query)  # for mobile cases , screen protectors , accessories mostly apple stuff

        # future = executor.submit(bouri, query) # for kitchen electronics 

    print(json.dumps(ProductsArr, ensure_ascii = True ))

if __name__ == "__main__":
    main(sys.argv[1])

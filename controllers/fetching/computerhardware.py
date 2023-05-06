from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
import json, sys, re,time

s = Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []

# s

def maximumhardware(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://maximumhardware.store/index.php?route=product/search&search=" + query
    driver.get(url)

    products = driver.find_element(By.CLASS_NAME, "main-products")
    products = products.find_elements(By.CLASS_NAME , "product-layout")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "name")
        try:
            price = product.find_element(By.CLASS_NAME , "price-new").text
        except:
            price = product.find_element(By.CLASS_NAME , "price-normal").text    
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "img-first").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Maximum Hardware",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()

def badrgroup(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://elbadrgroupeg.store/index.php?route=product/search&search=" + query
    driver.get(url)

    products = driver.find_element(By.CLASS_NAME, "main-products")
    products = products.find_elements(By.CLASS_NAME , "product-layout")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "name")
        try:
            price = product.find_element(By.CLASS_NAME , "price-new").text
        except:
            price = product.find_element(By.CLASS_NAME , "price-normal").text    
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "img-first").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Badr Group",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()

def sigma(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://www.sigma-computer.com/search?search={query}&submit_search=&route=product%2Fsearch'
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME, "product-item-container")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "caption")
        
        price = product.find_element(By.CLASS_NAME , "price-new").text
         
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "img-1").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text

        try: 
            outofstock = product.find_element(By.CLASS_NAME, "stock_N")
        except:
            ProductsArr.append({
                "Count" : i,
                "Shop"  : "Sigma",
                "Title" : title,
                "Price" : float(price),
                "Link"  : link,
                "Img"   : img
            } )
            i += 1
    driver.close()

def baraka(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://barakacomputer.net/searchproduct?search=" + query
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_element(By.ID, "store")
    products = products.find_elements(By.CLASS_NAME , "product")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-name")
        img = product.find_element(By.CLASS_NAME , "product-img").find_element(By.TAG_NAME, "img").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        try:
            price = product.find_element(By.CLASS_NAME , "product-price").text.split(" ")[0]
            price = re.sub(r"[^0-9\.]+" , '' , price)  
        except:
            price = 0    
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Baraka",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()


def compuscience(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://compuscience.com.eg/en/search?controller=search&orderby=position&orderway=desc&search_category=all&submit_search=&search_query={query}'
    driver.get(url)

    products = driver.find_element(By.ID, "products")
    products = products.find_elements(By.CLASS_NAME , "product-miniature")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-title")
        try:
            price = product.find_element(By.CLASS_NAME , "price").text
        except:
            price = 0   
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "thumbnail-inner").find_element(By.TAG_NAME, "img").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Compu Science",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()


def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(maximumhardware, query)
        future = executor.submit(badrgroup, query)  
        future = executor.submit(baraka, query) 
        # future = executor.submit(sigma, query) #slow af
        future = executor.submit(compuscience, query) 
      
    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = True ))
    # print(f'time : {end - start : .2f}') #avg 5 secs

if __name__ == "__main__":
    main(sys.argv[1])

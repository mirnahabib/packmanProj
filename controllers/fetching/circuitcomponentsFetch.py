from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
import json, sys, re , time

s = Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []

def futureElectronics(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://store.fut-electronics.com/search?type=product&q={query}'
    driver.get(url)
    time.sleep(1) # titles , prices returns empty without waiting

    products = driver.find_element(By.CLASS_NAME , "product-grid")
    products = products.find_elements(By.TAG_NAME,"div")


    for product in products[:20]:
        if product.get_attribute("class") == 'sold-out':
            continue
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.TAG_NAME , "h3").text
        price = product.find_element(By.TAG_NAME, "h4").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.TAG_NAME , "img").get_attribute("src")
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
        
        if (title != '' and price != ''):
            ProductsArr.append({
                "Count" : i,
                "Shop"  : "Future Electronics",
                "Title" : title,
                "Price" : float(price),
                "Link"  : link,
                "Img"   : img
            } )
            i += 1
    driver.close()        

def makersElectronics(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://makerselectronics.com/?term=&s={query}&post_type=product&taxonomy=product_cat'
    driver.get(url)    
    products = driver.find_elements(By.CLASS_NAME,"product-wrapper")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        if product.find_element(By.CLASS_NAME,"product-label").text == "Sold out":
            continue
        title = product.find_element(By.CLASS_NAME , "product-name")
        price = product.find_element(By.CLASS_NAME , "price")
        try:
            price = price.find_element(By.TAG_NAME , "ins").text  
        except:
            price = price.find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.CLASS_NAME , "thumbnail-wrapper").find_element(By.TAG_NAME,"img").get_attribute("src")
        link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = title.text
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Makers Electronics",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()

def ram(query):
    i=1
    options = Options()
    # options.add_argument('--headless')
    # options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://ram-e-shop.com/?s={query}&product_cat=0&post_type=product'
    driver.get(url)    
    products = driver.find_elements(By.CLASS_NAME , "product-type-simple")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "woocommerce-LoopProduct-link")
        price = product.find_element(By.CLASS_NAME , "price")
        try:
            price = price.find_element(By.TAG_NAME , "ins").text  
        except:
            price = price.find_element(By.CLASS_NAME, "woocommerce-Price-amount").text
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "attachment-woocommerce_thumbnail").get_attribute("src")
        link = title.get_attribute("href")
        title=title.text
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "RAM",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()    

    


def main(query):
   
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(futureElectronics, query)
        future = executor.submit(makersElectronics, query) 
        # future = executor.submit(ram, query) #empty titles 
    
        
    print(json.dumps(ProductsArr, ensure_ascii = True ))

if __name__ == "__main__":
    main(sys.argv[1])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from concurrent.futures import ThreadPoolExecutor
import json,sys , time , re

s=Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []

def amazon(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    searchedProduct = query
    url = f'https://www.amazon.eg/s?k={query}&i=grocery&language=en_AE'
    driver.get(url)
    products = driver.find_elements(By.CLASS_NAME,"a-spacing-base")

    for product in products[:20]:
        title = product.find_element(By.CLASS_NAME, "a-size-mini").text
        try:
            price = product.find_element(By.CLASS_NAME , "a-price-whole").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            continue
        link = product.find_element(By.CLASS_NAME , "s-product-image-container").find_element(By.TAG_NAME, "a").get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "s-product-image-container").find_element(By.TAG_NAME, "img").get_attribute("src")  

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Amazon",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close() 

def hyperone(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.hyperone.com.eg/search?q=" + query
    driver.get(url)
    driver.implicitly_wait(10)

    products = driver.find_elements(By.CLASS_NAME , "ProductCard")

    for product in products[:20]:
        title = product.find_element(By.CLASS_NAME , "ProductTitle").text
        price = product.find_element(By.XPATH , "./div[2]/a/div/div[1]").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = product.find_element(By.TAG_NAME , "a").get_attribute("href")
        img = product.find_element(By.TAG_NAME , "img").get_attribute("src")

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Hyperone",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def gourmet(query):
    i = 1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    
    url = "https://gourmetegypt.com/catalogsearch/result/?q=" + query
    driver.get(url)
    driver.implicitly_wait(3)
    allProducts = driver.find_element(By.CLASS_NAME, "products-group")
    products = allProducts.find_elements(By.CLASS_NAME , "product-item-info")


    # //*[@id="product-item-info_15619"]
    # //*[@id="product-item-info_15619"]/a/span/span/img

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-item-link").get_attribute("innerHTML")
        price = product.find_element(By.CLASS_NAME , "price").get_attribute("innerHTML")
        price = re.sub(r"[^0-9\.]" , '' , price)
        link = product.find_element(By.CLASS_NAME , "product-item-photo").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "product-image-photo").get_attribute("data-src")

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Gourmet",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def spinney(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://spinneys-egypt.com/en/search?term=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "sp-product")
    # driver.implicitly_wait(3)
    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "text-capitalize").text
        price = product.find_element(By.CLASS_NAME , "priceAfter").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = product.find_element(By.CLASS_NAME , "imgwrap").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "lazy").get_attribute("src")
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Spinney",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def carrefour(query):
    i=1 
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.carrefouregypt.com/mafegy/en/v4/search?keyword=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "css-b9nx4o")

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME , "css-tuzc44")
        price = product.find_element(By.CLASS_NAME , "css-17fvam3").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = title.find_element(By.XPATH , "./a").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "css-1npvvk7")
        pic = img.find_element(By.XPATH , "./a/img").get_attribute("src")
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Carrefour",
            "Title" : title.text,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : pic
        })
        i += 1
    driver.close()


def main(query):
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(hyperone, query)  
        future = executor.submit(gourmet, query)  
        # future = executor.submit(spinney, query)  
        future = executor.submit(carrefour, query) 
        future = executor.submit(amazon, query) 

    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = False ))
    # print(f'time : {end - start : .2f}')        #avg 7 secs

if __name__ == "__main__":
    main(sys.argv[1])

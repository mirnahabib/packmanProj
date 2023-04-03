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
import json,sys , time

s=Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []

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
        link = product.find_element(By.TAG_NAME , "a").get_attribute("href")
        img = product.find_element(By.TAG_NAME , "img").get_attribute("src")

        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Hyperone",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
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

    for product in products[:20]:
        title = product.find_element(By.CLASS_NAME , "product-item-link").get_attribute("innerHTML")
        price = product.find_element(By.CLASS_NAME , "price").get_attribute("innerHTML")
        link = product.find_element(By.CLASS_NAME , "product-item-photo").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "product-image-photo").get_attribute("src")

        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Gourmet",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
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
        link = product.find_element(By.CLASS_NAME , "imgwrap").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "lazy").get_attribute("src")
        
        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Spinney",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
        i += 1
    driver.close()

def carrefour(query):
    i=1 
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.carrefouregypt.com/mafegy/en/v4/search?keyword=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "css-b9nx4o")

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME , "css-1nhiovu")
        price = product.find_element(By.CLASS_NAME , "css-17fvam3").text
        link = title.find_element(By.XPATH , "./a").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "css-1itwyrf")
        pic = img.find_element(By.XPATH , "./a/img").get_attribute("src")
        
        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Carrefour",
            "Title" : title.text,
            "Price" : price,
            "Link"  : link,
            "Img"   : pic
        }])
        i += 1
    driver.close()


def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(hyperone, query)  
        future2 = executor.submit(gourmet, query)  
        future3 = executor.submit(spinney, query)  
        future4 = executor.submit(carrefour, query) 
    end = time.time()
    print(ProductsArr)
    print(f'time : {end - start : .2f}')        #avg 7 secs

if __name__ == "__main__":
    main(sys.argv[1])

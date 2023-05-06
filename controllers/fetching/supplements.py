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



def iherb(query):
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://eg.iherb.com/search?sug=magnesium&kw=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product-cell-container")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-title").text
        try:
            price = product.find_element(By.CLASS_NAME , "discount-red").text  
        except:
            price = product.find_element(By.CLASS_NAME , "price").text 
        price = re.sub(r"[^0-9\.]+" , '' , price)    
        img = product.find_element(By.CLASS_NAME , "product-image").find_element(By.TAG_NAME,"img").get_attribute("src")
        link = product.find_element(By.CLASS_NAME, "product-link").get_attribute("href")
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "iHerb",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()
# ss 
def biovea(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://www.biovea.com/eg/productlist/results?KW={query}"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"prod-card--dispatch")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "prod-card__title")
        try:
            price = product.find_element(By.CLASS_NAME , "prod-pricing__savings--pack").text.split(" ")[2]
        except:
            price = product.find_element(By.CLASS_NAME , "our-price").text.split(" ")[0]
        price = re.sub(r"[^0-9\.]+" , '' , price)  
        link = title.find_element(By.TAG_NAME , "a").get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "prod-card__image").find_element(By.TAG_NAME,"img").get_attribute("src")  
        title = title.text
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Biovea",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()     


def main(query):

    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(iherb, query)
        future = executor.submit(biovea, query)  # bottleneck 

    print(json.dumps(ProductsArr, ensure_ascii = True ))

if __name__ == "__main__":
    main(sys.argv[1])

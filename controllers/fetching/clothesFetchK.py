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
    url = f"https://www.amazon.eg/s?k={query}&rh=n%3A21845143031&language=en_AE&ref=nb_sb_noss"  
    driver.get(url)
    products = driver.find_elements(By.CLASS_NAME,"a-spacing-base")

    for product in products[:20]:
        try:
            isSponsered = product.find_element(By.CLASS_NAME , "puis-label-popover-default")  
            continue  
        except:
            pass
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

def jumia(query):
    i = 1
    options = Options()
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)

    url = f"https://www.jumia.com.eg/category-fashion-by-jumia/?q={query}&gender=Kids#catalog-listing" 
    driver.get(url)
    popup = driver.find_element(By.CLASS_NAME,"cw")
    popup.find_element(By.XPATH,"./button").click()

    products = driver.find_elements(By.CLASS_NAME,"c-prd")

    for product in products[:20]:
        title = product.find_element(By.CLASS_NAME,"name").text
        price = product.find_element(By.CLASS_NAME,"prc").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = product.find_element(By.CLASS_NAME,"core").get_attribute("href")
        img = product.find_element(By.XPATH,"./a/div[1]/img").get_attribute("data-src")
    
        ProductsArr.append({
        "Count" : i,
        "Shop"  : "Jumia",
        "Title" : title,
        "Price" : float(price),
        "Link"  : link,
        "Img"   : img
        })
        i += 1
    driver.close() 


def zara(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = f'https://www.zara.com/eg/en/search?searchTerm={query}&section=KID'
    driver.get(url)
    driver.implicitly_wait(3)

    products = driver.find_elements(By.CLASS_NAME , "product-grid-product")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-grid-product-info__name")
        price= product.find_element(By.CLASS_NAME, "money-amount__main").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = title.get_attribute("href")
        img = product.find_element(By.CLASS_NAME, "media-image__image").get_attribute("src")

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Zara",
            "Title" : title.text,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def max(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs) 
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://www.maxfashion.com/eg/en/search?q={query}%20:allCategories:mxkids'
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.XPATH , './div[3]').text
        price = product.find_element(By.XPATH , './div[2]').text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img_link = product.find_element(By.XPATH , "./div[1]")
        link = img_link.find_element(By.TAG_NAME , "a").get_attribute("href")
        imgs = img_link.find_elements(By.TAG_NAME , "img")
        img= imgs[1].get_attribute("src")
    
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Max",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def handm(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = f'https://eg.hm.com/en/#query={query}&hierarchicalMenu%5Bfield_category.lvl0%5D=Kids&page=1'
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "c-products__item") 

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME, "field--name-name").text
        try:
            price = product.find_element(By.CLASS_NAME, "special--price").text
        except:
            price = product.find_element(By.CLASS_NAME, "price").text    
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.TAG_NAME , "img").get_attribute('src')
        link = product.find_element(By.TAG_NAME , "a").get_attribute("href")

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "H&M",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()
    
def lcwaikiki(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    
    url = f"https://www.lcwaikiki.eg/en-US/EG/search?q={query} kid"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"product-card")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "product-card__title").text
        try:
            price = product.find_element(By.CLASS_NAME , "product-price__cart-price").text
            price = price.replace(",", ".")
        except:
            price = product.find_element(By.CLASS_NAME , "product-price__price").text
            
        price = re.sub(r"[^0-9\.]+" , '' , price)  
        link = product.find_element(By.TAG_NAME , "a").get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "product-image__image").get_attribute("src")  

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Lc Waikiki",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()

def adidas(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = f'https://www.adidas.com.eg/en/kids-search?q={query}'
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product-tile") 

    for product in products[:20]: 
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "link")
        price = product.find_element(By.CLASS_NAME, "sales").text  
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.CLASS_NAME , "tile-image").get_attribute('src')
        link = title.get_attribute("href")
        title = title.text

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Adidas",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()


def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=30) as executor:
        future = executor.submit(zara, query)  
        future = executor.submit(amazon, query)  
        future = executor.submit(jumia, query)  
        future = executor.submit(adidas, query)
        future = executor.submit(handm, query)  
        future = executor.submit(max, query)  
        future = executor.submit(lcwaikiki, query) 
    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = False ))
    # print(f'time : {end - start : .2f}')     #avg 10 secs

if __name__ == "__main__":
    main(sys.argv[1])

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
import json,sys ,time , re


s = Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
ProductsArr = []


def amazon(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    
    url = f'https://www.amazon.eg/s?k={query}&i=beauty&language=en_AE'
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

def jumia(query):
    i = 1
    options = Options()
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)

    url = f'https://www.jumia.com.eg/health-beauty/?q={query}'
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

def noon(query):
    i=1
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = f'https://www.noon.com/egypt-en/beauty-and-health/?limit=20&q={query}'
    driver.get(url)
    driver.implicitly_wait(10)
    products = driver.find_elements(By.CLASS_NAME, "productContainer")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        link = product.find_element(By.TAG_NAME , "a")
        title = link.find_element(By.XPATH , "./div/div/div[2]/div[1]").get_attribute("title")
        price = product.find_element(By.CLASS_NAME , "amount").text
        linkURL= link.get_attribute("href")
        try:
            img = link.find_element(By.CLASS_NAME,"lazyload-wrapper").find_element(By.TAG_NAME, "img").get_attribute("src")
            
        except:
            img = None
               
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Noon",
            "Title" : title,
            "Price" : float(price),
            "Link"  : linkURL,
            "Img"   : img
        })
        i += 1
    driver.close()
    
def faces(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.faces.com/eg-en/search?q=" + query
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"js-product-tile")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "product-tile-name-text").text
        price = product.find_element(By.CLASS_NAME , "js-price").text            
        price = re.sub(r"[^0-9\.]+" , '' , price)  
        link = product.find_element(By.CLASS_NAME , "product-tile-link").get_attribute("href")
        img =  product.find_element(By.CLASS_NAME , "tile-image").get_attribute("src")  

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Faces",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()        

def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(amazon, query)  
        future = executor.submit(jumia, query)  
        future = executor.submit(faces, query)
        future = executor.submit(noon, query) #noon sometimes runs into problems
    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = True ))
    # print(f'time : {end - start : .2f}') #avg 5 secs

if __name__ == "__main__":
    main(sys.argv[1])

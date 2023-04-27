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



def olx(query):
    query = query.replace(" " , "-")
    i=1
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.olx.com.eg/en/ads/q-" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "_7e3920c1")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "a5112ca8").text
        try:
            price = product.find_element(By.CLASS_NAME , "_95eae7db").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            price = 0    
        img = product.find_element(By.CLASS_NAME , "_76b7f29a").get_attribute("src")
        link = product.find_element(By.CLASS_NAME, "ee2b0479").find_element(By.TAG_NAME, "a").get_attribute("href")
        
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "OLX",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        } )
        i += 1
    driver.close()

def opensooq(query):
    i = 1    
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs) #this line disables image loading to reduce network workload
    driver = webdriver.Chrome(service=s , options=options)
    url = f"https://eg.opensooq.com/en/find?PostSearch[term]={query}"
    driver.get(url)
    driver.implicitly_wait(5)
    products = driver.find_elements(By.CLASS_NAME,"mb-32")
    driver.implicitly_wait(0)

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME, "breakWord").text
        try:
            price = product.find_element(By.CLASS_NAME , "postPrice").text
            price = re.sub(r"[^0-9\.]+" , '' , price)  
        except:
            price = 0

        link = product.find_element(By.CLASS_NAME , "grayHoverBg")
        img =  link.find_element(By.XPATH , "./div[1]/img").get_attribute("src")  
        link = link.get_attribute('href')
        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Open Sooq",
            "Title" : title,
            "Price" : float(price),
            "Link"  : link,
            "Img"   : img
        })
        i += 1
    driver.close()     


def main(query):
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(olx, query)
        future = executor.submit(opensooq, query)  

    print(json.dumps(ProductsArr, ensure_ascii = True ))

if __name__ == "__main__":
    main(sys.argv[1])

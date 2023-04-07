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

def bershka(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.bershka.com/eg/en/q/" + query
    driver.get(url)
    driver.implicitly_wait(15)

    # gender = driver.find_element(By.CLASS_NAME, "gender-filters")
    # men = gender.find_element(By.XPATH , "./button[3]").click()
    # women = gender.find_element(By.XPATH , "./button[2]")

    products = driver.find_elements(By.CLASS_NAME , "search-product-card")


    for product in products[1:21]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-text").text
        price = product.find_element(By.CLASS_NAME, "current-price-elem").text
        img = product.find_element(By.CLASS_NAME , "image-item").get_attribute("src")
        link = product.find_element(By.CLASS_NAME , "grid-card-link").get_attribute("href")

        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Bershka",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
        i += 1
    driver.close()

def zara(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.zara.com/eg/en/search?searchTerm=" + query
    driver.get(url)
    driver.implicitly_wait(3)

    products = driver.find_elements(By.CLASS_NAME , "product-grid-product")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "product-grid-product-info__name")
        price = product.find_element(By.CLASS_NAME, "money-amount__main").text
        link = title.get_attribute("href")
        img = product.find_element(By.CLASS_NAME, "media-image__image").get_attribute("src")

        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Zara",
            "Title" : title.text,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
        i += 1
    driver.close()

def max(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.maxfashion.com/eg/en/search?q=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "product")

    for product in products[:20]:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.XPATH , './div[3]').text
        price = product.find_element(By.XPATH , './div[2]').text
        img_link = product.find_element(By.XPATH , "./div[1]")
        link = img_link.find_element(By.TAG_NAME , "a").get_attribute("href")
        imgs = img_link.find_elements(By.TAG_NAME , "img")
        img= imgs[1].get_attribute("src")
    
        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "Max",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
        i += 1
    driver.close()

def handm(query):
    i=1
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://eg.hm.com/en/#query=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "c-products__item") 

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME, "field--name-name").text
        price = product.find_element(By.CLASS_NAME, "price").text
        img = product.find_element(By.TAG_NAME , "img").get_attribute('src')
        link = product.find_element(By.TAG_NAME , "a").get_attribute("href")

        ProductsArr.append([{
            "Count" : i,
            "Shop"  : "H&M",
            "Title" : title,
            "Price" : price,
            "Link"  : link,
            "Img"   : img
        }])
        i += 1
    driver.close() 


def main(query):
    start = time.time()
    with ThreadPoolExecutor(max_workers=25) as executor:
        future = executor.submit(zara, query)  
        future2 = executor.submit(handm, query)  
        future3 = executor.submit(max, query)  
        future4 = executor.submit(bershka, query) 
    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = False ).encode('utf-8').decode())
    print(f'time : {end - start : .2f}')     #avg 10 secs

if __name__ == "__main__":
    main(sys.argv[1])

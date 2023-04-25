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
    searchedProduct = query
    url = "https://www.amazon.eg/-/en/s?k=" + searchedProduct
    driver.get(url)
    products = driver.find_elements(By.CLASS_NAME,"a-spacing-base")

    for product in products[:20]:
        title = product.find_element(By.CLASS_NAME, "a-size-mini").text
        try:
            price = product.find_element(By.CLASS_NAME , "a-price-whole").text
            price = re.sub(r"[^0-9\.]+" , '' , price)
        except:
            price = 0
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

    url = "https://www.jumia.com.eg/catalog/?q=" + query
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
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.noon.com/egypt-en/search/?q=" + query
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
        price = re.sub(r"[^0-9\.]+" , '' , price)
        img = product.find_element(By.CLASS_NAME , "image-item").get_attribute("src")
        link = product.find_element(By.CLASS_NAME , "grid-card-link").get_attribute("href")

        ProductsArr.append({
            "Count" : i,
            "Shop"  : "Bershka",
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
    # options.add_argument('--headless')
    # options.add_experimental_option("prefs", prefs) doesn't work with max, gets max's logo imgs 
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    url = "https://www.maxfashion.com/eg/en/search?q=" + query
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
    url = "https://eg.hm.com/en/#query=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "c-products__item") 

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME, "field--name-name").text
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
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    url = "https://www.carrefouregypt.com/mafegy/en/v4/search?keyword=" + query
    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME , "css-b9nx4o")

    for product in products[:20]: 
        title = product.find_element(By.CLASS_NAME , "css-1nhiovu")
        price = product.find_element(By.CLASS_NAME , "css-17fvam3").text
        price = re.sub(r"[^0-9\.]+" , '' , price)
        link = title.find_element(By.XPATH , "./a").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "css-1itwyrf")
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
    with ThreadPoolExecutor(max_workers=40) as executor:
        future = executor.submit(amazon, query)  
        future = executor.submit(jumia, query)  
        future = executor.submit(noon, query) #noon sometimes runs into problems
        future = executor.submit(bershka, query)  
        future = executor.submit(zara, query)  
        future = executor.submit(max, query)  
        future = executor.submit(handm, query)  
        future = executor.submit(hyperone, query)  
        future = executor.submit(gourmet, query)  
        future = executor.submit(spinney, query)  
        future = executor.submit(carrefour, query)  

    end = time.time()
    print(json.dumps(ProductsArr, ensure_ascii = True ))
    # print(f'time : {end - start : .2f}') #avg 5 secs

if __name__ == "__main__":
    main(sys.argv[1])

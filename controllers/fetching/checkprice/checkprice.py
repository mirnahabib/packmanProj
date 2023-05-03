from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
import json,sys,time,re

s = Service(ChromeDriverManager().install())
prefs = {"profile.managed_default_content_settings.images": 2}
the_price = []


def amazon(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)
    product = driver.find_element(By.ID, "ppd")

    price = product.find_element(
        By.CLASS_NAME, "a-price").find_element(By.XPATH, "./span[2]").text
    if "\n" in price:
        price = price.split("\n")[0]
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()


def jumia(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    product = driver.find_element(By.CLASS_NAME, "card")
    price = product.find_element(By.CLASS_NAME, "-mtxs")
    price = price.find_element(
        By.XPATH, "./div/span").text
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()

def noon(link):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "priceNow").text
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()

def dubaiphone(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "oe_price").text
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()

def _2B(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "price-box")
    try:
        price = price.find_element(By.CLASS_NAME, "special-price").text
    except:
        price = price.find_element(By.CLASS_NAME, "price").text    

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()    

def select(link):
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)
    price = driver.find_element(By.CLASS_NAME, "price").text

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()

def zara(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME , "money-amount__main").text
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()

def max(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36") 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.ID , "details-price").text
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()

def handm(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "content-sidebar-wrapper")
    try : 
        price = product.find_element(By.CLASS_NAME, "special--price").text
    except:
        price = product.find_element(By.CLASS_NAME , "price-amount").text    
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()    

def townteam(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "tt-product-single-info")
    try : 
        price = product.find_element(By.CLASS_NAME, "sale-price").text
    except:
        price = product.find_element(By.CLASS_NAME , "new-price").text    
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

def lcwaikiki(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.ID, "priceAreaProductDetail") 
    try : 
        price = product.find_element(By.CLASS_NAME, "basket-discount").text
        if "." in price:
            price = price.replace(".","")
        price = price.replace(",",".")
    except:
        price = product.find_element(By.CLASS_NAME , "single-price").text    
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

def bershka(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "current-price-elem").text   
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

# def brantu(link):
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging']) 
#     # options.add_argument('--headless')
#     # options.add_experimental_option("prefs", prefs)
#     driver = webdriver.Chrome(service=s , options=options)
#     driver.get(link)
#     driver.implicitly_wait(3)

#     product = driver.find_element(By.CLASS_NAME , "box")
#     price = product.find_element(By.CLASS_NAME, "style__Price-cie3jr-16").text   
    
#     price = re.sub(r"[^0-9\.]+", '', price)

#     the_price.append({
#         "Price": float(price),
#     })
    
#     driver.close()    

def faces(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "product-info-container")
    try:
        price = product.find_element(By.CLASS_NAME, "price-on-sale").text
    except:    
        price = product.find_element(By.CLASS_NAME, "price").text
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()    

def ikea(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "pip-temp-price-module__current-price")
    price = price.find_element(By.CLASS_NAME , "pip-temp-price__integer").text
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()       

def hubfurniture(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    try:
        price = driver.find_element(By.CLASS_NAME , "special-price").text
    except:
        price = driver.find_element(By.CLASS_NAME, "price").text

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()

def carrefour(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "css-1oh8fze")

    try :
        price = price.find_element(By.CLASS_NAME, "css-1i90gmp").text
        price = price.split(" ")[1]
    except:
        price = price.find_element(By.CLASS_NAME, "css-17ctnp").text  
        price = price.split(" ")[1]
        price = price.split("(")[0]

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()  

def spinney(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "details")
    price = product.find_element(By.CLASS_NAME, "product-price")

    try:
        price = price.find_element(By.CLASS_NAME , "special-price").text
    except:
        price = price.text

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

def gourmet(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "product-info-main")
    price = product.find_element(By.CLASS_NAME, "price").text

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()          

def hyperone(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "ProductSummary")
    price = product.find_element(By.XPATH, "./div[2]/div[1]").text
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()  

def games2egypt(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "productDetails_price").text

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

def egygamer(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    product = driver.find_element(By.CLASS_NAME, "product-info-main")
    try:
        price = product.find_element(By.CLASS_NAME, "special-price").text
    except:    
        price = product.find_element(By.CLASS_NAME, "price").text

    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close() 

def shamy(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "product-form__info-content")
    price = price.find_element(By.CLASS_NAME, "price").text
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()     

def gameworld(link):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) 
    options.add_argument('--headless')
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s , options=options)
    driver.get(link)
    driver.implicitly_wait(3)

    price = driver.find_element(By.CLASS_NAME, "pro_price").text
    
    price = re.sub(r"[^0-9\.]+", '', price)

    the_price.append({
        "Price": float(price),
    })
    
    driver.close()      

def main(link):
    start = time.time()
    # gameworld(link)
    # shamy(link)
    # egygamer(link)
    # games2egypt(link)
    # hyperone(link)
    # gourmet(link)
    # spinney(link)
    # carrefour(link)
    # hubfurniture(link)
    # ikea(link)
    # faces(link)
    # brantu(link) <- not working yet
    # bershka(link)
    # lcwaikiki(link)
    # townteam(link)
    # handm(link)
    # max(link)
    # zara(link)
    # amazon(link)
    # jumia(link)
    # noon(link)
    # dubaiphone(link)
    # _2B(link)
    # select(link)


    end = time.time()
    print(json.dumps(the_price, ensure_ascii=True))

    # print(f'time : {end - start : .2f}')     #avg 10 secs


if __name__ == "__main__":
    main(sys.argv[1])

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

    price = driver.find_element(By.CLASS_NAME, "priceToPay").find_element(By.CLASS_NAME, "a-price-whole").text
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

def btech(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)
    product = driver.find_element(By.CLASS_NAME, "product-info-price")
    try:
        price = product.find_element(By.CLASS_NAME, "non_dealer_price")
        price = price.find_element(By.CLASS_NAME, "price-huge-static").text
    except:
        price = driver.find_element(By.CLASS_NAME, "price-huge-static").text
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": (price),
    })

    driver.close()

def dream2000(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

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

def maximumhardware(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    product = driver.find_element(By.CLASS_NAME, "price-group")
    try:
        price = product.find_element(By.CLASS_NAME, "product-price-new").text
    except:
        price = product.text        

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()   

def baraka(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "product-price").text
          
    price = price.split(" ")[0]
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()   

def sigma(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "product_page_price").text
          
    price = price.split(" ")[0]
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()   

def compuscience(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "current-price-display").text
          
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()       

def iherb(link):
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    product = driver.find_element(By.CLASS_NAME, "product-action-container")
    
    try:
        price = product.find_element(By.CLASS_NAME, "s24").text
    except:
        price = product.find_element(By.CLASS_NAME, "price-inner-text").text   

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()    

def biovea(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "price--our-price").text
    price = price.split(" ")[0]    

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()       

def nowfoodsegypt(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    product = driver.find_element(By.CLASS_NAME , "product-page-price")

    try:
        price = product.find_element(By.TAG_NAME , "ins").text  
    except:
        price = product.find_element(By.CLASS_NAME, "woocommerce-Price-amount").text   

    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()   

def future(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "product-price").text
        
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()    

def makers(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    product = driver.find_element(By.CLASS_NAME , "entry-summary")
    price = product.find_element(By.CLASS_NAME, "price")

    try:
        price = price.find_element(By.TAG_NAME , "ins").text  
    except:
        price = price.find_element(By.CLASS_NAME, "woocommerce-Price-amount").text 
        
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close()  

def americaneagle(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    try : 
        price = driver.find_element(By.CLASS_NAME, "special--price").text
    except:
        price = driver.find_element(By.CLASS_NAME , "price-amount").text 
        
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close() 

def adidas(link):
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "prices").find_element(By.CLASS_NAME , "sales").find_element(By.CLASS_NAME, "value").get_attribute("content")
        
    price = re.sub(r"[^0-9\.]+", '', price)
    the_price.append({
        "Price": float(price),
    })

    driver.close() 

def activ(link):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(link)

    price = driver.find_element(By.CLASS_NAME, "price-item--regular").text
    if (price == ""):
        price = driver.find_element(By.CLASS_NAME, "price-item--sale").text
    price = re.sub(r"[^0-9\.]+" , '' , price)
        
    the_price.append({
        "Price": float(price),
    })

    driver.close()     
 

def main(link, store):
    start = time.time()
    switch = {
        "Amazon": amazon,
        "Noon": noon,
        "Jumia": jumia,
        "Dubai phone": dubaiphone,
        "B.Tech" : btech,
        "2B": _2B,
        "Dream2000": dream2000,
        "Select": select,
        "Zara": zara,
        "Max": max,
        "H&M": handm,
        "Town Team": townteam,
        "Lc Waikiki": lcwaikiki,
        "Bershka": bershka,
        # "Brantu": bershka,
        "Faces": faces,
        "Ikea": ikea,
        "Hub furniture": hubfurniture,
        "Carrefour": carrefour,
        "Spinney": spinney,
        "Gourmet": gourmet,
        "Hyperone": hyperone,
        "Games2Egypt": games2egypt,
        "Egygamer": egygamer,
        "Shamy": shamy,
        "Game World": gameworld,
        "Maximum Hardware": maximumhardware,
        "Badr Group": maximumhardware,
        "Baraka" : baraka,
        "Sigma": sigma,
        "Compu Science": compuscience,
        "iHerb":iherb, # only work without headless
        "Biovea": biovea,
        "Now Foods Egypt": nowfoodsegypt,
        "Future Electronics" : future,
        "Makers Electronics" : makers,
        "RAM" : makers,
        "American Eagle" : americaneagle,
        "Adidas" : adidas, # only work without headless
        "Activ" : activ,

    }
    switch.get(store)(link)

    end = time.time()
    print(json.dumps(the_price, ensure_ascii=True))

    # print(f'time : {end - start : .2f}')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
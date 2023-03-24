from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import json , time , sys

def main(searchitem):
    searchitem = searchitem.replace(" " , "-")

    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = searchitem
    url = "https://www.olx.com.eg/en/ads/q-" + searchedProduct
    driver.get(url)
    # body = driver.find_element(By.TAG_NAME , "body")
    # body.click
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    products = driver.find_elements(By.CLASS_NAME , "_7e3920c1")

    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "a5112ca8").text
        try:
            price = product.find_element(By.CLASS_NAME , "_95eae7db").text
        except:
            price = "Seller didn't add the price"    
        img = product.find_element(By.CLASS_NAME , "_76b7f29a").get_attribute("src")
        link = product.find_element(By.CLASS_NAME, "ee2b0479").find_element(By.TAG_NAME, "a").get_attribute("href")
        
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link) 

    ProductsArr = [{ "Shop":"OLX" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    x = json.dumps(ProductsArr)
    print(x)     

if __name__ == "__main__":
    word = sys.argv[1]
    main(word)

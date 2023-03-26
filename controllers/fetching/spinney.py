from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json , sys
from selenium.webdriver.common.action_chains import ActionChains


def main(searchitem):

    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = searchitem
    url = "https://spinneys-egypt.com/en/search?term=" + searchedProduct
    driver.get(url)


    products = driver.find_elements(By.CLASS_NAME , "sp-product")
    # driver.implicitly_wait(3)
    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "text-capitalize").text
        price = product.find_element(By.CLASS_NAME , "priceAfter").text
        link = product.find_element(By.CLASS_NAME , "imgwrap").get_attribute("href")
        img = product.find_element(By.CLASS_NAME , "lazy").get_attribute("src")
        
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Spinney" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

if __name__ == "__main__":
    main(sys.argv[1])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import sys



def main(searchitem):
    
    tit , pri , imgref , productURL= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = searchitem
    url = "https://www.noon.com/egypt-en/search/?q=" + searchedProduct
    driver.get(url)
    driver.implicitly_wait(10)
    products = driver.find_elements(By.CLASS_NAME, "productContainer")

    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.CLASS_NAME , "sc-5e50ccb9-20").get_attribute("title")
        price = product.find_element(By.CLASS_NAME , "sc-6073040e-1").text
        link = product.find_element(By.XPATH , "./a")
        linkURL= link.get_attribute("href")
        try:
            img = link.find_element(By.CLASS_NAME,"lazyload-wrapper").find_element(By.TAG_NAME, "img").get_attribute("src")
            
        except:
            img = None
               
        tit.append(title)
        pri.append(price)
        imgref.append(img)
        productURL.append(linkURL) 

    ProductsArr = [{"Shop":"Noon", "Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,productURL)]
    print(ProductsArr)     
    



if __name__ == "__main__":
    main(sys.argv[1])


# //*[@id="__next"]/div/section/div/div/div/div[2]/div[1]/span[1]
# //*[@id="productBox-Z6FF92F2C4AC9041D5CB1Z"]
# //*[@id="productBox-Z6FF92F2C4AC9041D5CB1Z"]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div
# //*[@id="productBox-Z6FF92F2C4AC9041D5CB1Z"]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/img
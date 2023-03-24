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

    tit , pri , imgref , prodlink= [] , [] , [] , []

    ProductsArr = None
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(service=s , options=options)
    driver.maximize_window()
    searchedProduct = searchitem
    url = "https://www.maxfashion.com/eg/en/search?q=" + searchedProduct
    driver.get(url)

    # body = driver.find_element(By.TAG_NAME , "body")
    # body.click
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    # time.sleep(1)
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()



    products = driver.find_elements(By.CLASS_NAME , "product")


    for product in products:
        ActionChains(driver).scroll_to_element(product).perform()
        title = product.find_element(By.XPATH , './div[3]')
        price = product.find_element(By.XPATH , './div[2]')
        img_link = product.find_element(By.XPATH , "./div[1]")
        link = img_link.find_element(By.TAG_NAME , "a").get_attribute("href")
        imgs = img_link.find_elements(By.TAG_NAME , "img")
        img= imgs[1].get_attribute("src")
    
        
        tit.append(title.text)
        pri.append(price.text)
        imgref.append(img)
        prodlink.append(link)

    ProductsArr = [{ "Shop":"Max" ,"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
    print(ProductsArr)

if __name__ == "__main__":
    main(sys.argv[1])




# //*[@id="prodItemImgLink0"]
# //*[@id="prodItemImgLink0"]/img

#//*[@id="product-B22WUBNFEJEX154WHITEMULTISHADE"]
#//*[@id="prodItemImgLink8"]
#//*[@id="product-B22WUBNFEJEX154WHITEMULTISHADE"]/div[1]
#//*[@id="prodItemImgLink8"]/div[1]
#//*[@id="prodItemImgLink8"]
#//*[@id="prodItemImgLink8"]/img

#//*[@id="product-B22WCTFEWDDR253GREENLIGHT"]
#//*[@id="product-B22WCTFEWDDR253GREENLIGHT"]/div[3]
#//*[@id="product-B22WCTFSKD245GREENDARK"]/div[2]
#//*[@id="product-B22WCTFEWDDR253GREENLIGHT"]/div[3]
#

#//*[@id="product-WN21KD243CTBROWNMEDIUM"]
#//*[@id="product-WN21KD243CTBROWNMEDIUM"]/div[3]


#//*[@id="product-B22WUBNFEJEX154WHITEMULTISHADE"]
#//*[@id="product-B22WUBNFEJEX154WHITEMULTISHADE"]/div[1]
#//*[@id="prodItemImgLink8"]

#//*[@id="product-B22WCTFEWDDR253PINKLIGHT"]
#//*[@id="product-B22WCTFEWDDR253PINKLIGHT"]/div[1]
# //*[@id="product-B22WCTFEWDDR253PINKLIGHT"]/div[1]/a/img
#
#//*[@id="prodItemImgLink3"]

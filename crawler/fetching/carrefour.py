from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

tit , pri , imgref , prodlink= [] , [] , [] , []


ProductsArr = None
s=Service(ChromeDriverManager().install())
options = Options()
options.headless = False
driver = webdriver.Chrome(service=s , options=options)
searchedProduct = "chocolate"
url = "https://www.carrefouregypt.com/mafegy/en/v4/search?keyword=" + searchedProduct
driver.get(url)


products = driver.find_elements(By.CLASS_NAME , "css-b9nx4o")

for product in products: 
    title = product.find_element(By.CLASS_NAME , "css-1nhiovu")
    price = product.find_element(By.CLASS_NAME , "css-17fvam3").text
    link = title.find_element(By.XPATH , "./a").get_attribute("href")
    img = product.find_element(By.CLASS_NAME , "css-1itwyrf")
    pic = img.find_element(By.XPATH , "./a/img").get_attribute("src")
    
    tit.append(title.text)
    pri.append(price)
    imgref.append(pic)
    prodlink.append(link)

ProductsArr = [{"Title": t, "Price": p, "Img": img , "link": pLink} for t, p, img ,pLink in zip(tit,pri,imgref,prodlink)]
print(ProductsArr)







# //*[@id="__next"]/div[3]/div/div[3]/div[2]/div[3]/ul/div/div[1]/div/div/div[1]/div/ul/div[2]/div[3]/div[1]
# //*[@id="__next"]/div[3]/div/div[3]/div[2]/div[3]/ul/div/div[1]/div/div/div[1]/div/ul/div[2]/div[3]/div[1]/a

#//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[3]/ul/div/div[1]/div/div/div[1]/div/ul/div[2]/div[1]/div
#//*[@id="__next"]/div[3]/div/div[3]/div[2]/div[3]/ul/div/div[1]/div/div/div[1]/div/ul/div[2]/div[1]/div/a/img
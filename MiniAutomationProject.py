from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re
import sys

driver = webdriver.Chrome()
driver.maximize_window()

#variable contains URL
url = "https://www.amazon.in/"

#set instance
x = '0' 

#variable with brand
brand = "Galax"

#Webapp URL
driver.get(url)

#DriverWait expects additional round brackets around locator

WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))).send_keys("graphics card rtx 4060")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys(Keys.ENTER)

for x in range (1, 20):

#use f string to pass the instance dynamically
        element = driver.find_element(By.XPATH, f"(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[{x}]").text
        print(element)
         #look for a specific graphics card brand using RegEx (.search)
        match_result = re.search(f"{brand}", element)
        #if match found, break
        if(match_result) != None:
                break
        
if (match_result) == None:

        driver.quit(f"Graphics cards based on {brand} brand not found")
else:
                
        print(match_result)
                

#Break out of the loop when desired graphics card brand is found and open the product description page    
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, f"(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[{x}]"))).click()
sleep(5)

#Switch to active tab
driver.switch_to.window(driver.window_handles[1])

#Check for availability
stock = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-success']").text
print(stock)

stock_result = re.search("In stock", stock)

#If the product is in stock, add to cart. Else exit

if stock_result != None:

        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='add-to-cart-button']"))).click()

else:
        print("Product is out of stock")
        driver.quit()

#Verify product added to cart
sleep(5)
addedToCart = driver.find_element(By.XPATH, "//h1[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']").text
assert addedToCart == "Added to cart"

#Exit
driver.quit()

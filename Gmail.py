#import prereqs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#configure browser
Options=Options()
Options.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(Options)
#driver.maximize_window()

#options.add_argument("--user-data-dir=C:\\Users\\saive\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

#launch URL


driver.get("https://mail.google.com/mail/u/0/#inbox")

#login


#wait for page to load, look for compose button
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Compose']")))

assert element.is_displayed()


file = open("C:\\Users\\saive\\OneDrive\\desktop\\NewDoc.txt", "r")

for a in file:
        #click on Compose button
        driver.find_element(By.XPATH, "//div[text()='Compose']").click()
        sleep(3)
        #Enter receipient's email address
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='To recipients']"))).send_keys(f"{a}")
        sleep(3)
        #Enter subject
        element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='subjectbox']"))).send_keys("Test Subject")
        #Enter message body
        element = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Message Body']"))).send_keys("Hi This is a test email")
        #click send
        element = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='dC']/div[contains(@aria-label,'Send')]"))).click()
        sleep(3)
        #close sent notification
        element = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bBe']"))).click()
        sleep(5)




##selenium using wait function
##webwait function will wait until the task gets completed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://www.google.com/earth/"
driver=webdriver.Chrome(r"C:/Users/Lenovo/Desktop/chromedriverforpython/chromedriver")
driver.get(url)
wait=WebDriverWait(driver,100)   ##(url,secs)
launchEarthButton=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()


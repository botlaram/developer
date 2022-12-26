##drag and drop in weburl using selenium
##donwload google chrome driver for executing this script

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains ##Actionchain module is use for drag and drop

##provide the google chrome driver path
driver_path=r"C:/Users/Lenovo/Desktop/chromedriverforpython/chromedriver"
driver=webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

##for drag and drop we need src and dest path
##to get xpath value after inscept select the element uh want to drag and left click in inspect and copy the xpath
src=driver.find_element("xpath", '//*[@id="box3"]')
dest=driver.find_element("xpath", '//*[@id="box103"]')

actions=ActionChains(driver)
actions.drag_and_drop(src,dest).perform()


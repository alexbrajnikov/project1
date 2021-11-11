import driver as driver
from selenium import webdriver

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")





action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element(By.ID, "double-click")).perform()
alert = driver.switch_to.alert
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept() 

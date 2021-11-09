from selenium import webdriver
import time
from selenium.webdriver.common.by imports By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
list = []
items = driver.find_elements(By.CSS_SELECTOR,"div.inventory_item")
for item in items:
    item.click
names = driver.find_elements(By.CSS_SELECTOR,"div.inventory_item_name")
for name in names:
    list.append(name.text)
    
print(list)

list1 = []
driver.find_element(By.LINK_TEXT,"shopping_cart_link").click()

items_in_cart = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_name")
for item_in_cart in items_in_cart:
    list1.append(items_in_cart.text) 
    
print(list1)

assert list == list1

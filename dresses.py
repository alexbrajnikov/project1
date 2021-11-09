from selenium import webdriver
import time
from selenium.webdriver.common.by imports By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

list = []
list1 = []
driver=webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("http://automationpractice.com/index.php")
driver.find_element(By.NAME, "search_query").send_keys("dress"+ Keys.ENTER)
dresses = driver.find_elements(By.XPATH, "//ul[@class='product_list grid row']/li//h5")
for dress in dresses:
    list.append(dress.text)
print(list)
    
action = ActionChains(driver)
items = driver.find_elements(By.XPATH, "//ul[@class='product_list grid row']/li")
for item in items:
    action.move_to_element(item).perform()
    action.move_to_element(driver.find_element(By.XPATH, "span[@text()='Add to cart']")).click().perform()
    action.move_to_element(driver.find_element(By.XPATH, "//span[@title='Continue shopping']")).click().perform()
    
driver.find_element(By.CSS_SELECTOR, "a[title='View my shopping cart']").click()

items_in_cart = driver.find_element(By.CSS_SELECTOR, "td.cart_description")
for item_in_cart in items_in_cart:
    list1.append(item_in_cart.text)
    
print(list1)

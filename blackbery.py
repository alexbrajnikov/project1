from selenium import webdriver
import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
cart_element = driver.find_element(By.XPATH, "//h4/a[@href='#']").text
assert cart_element == "Blackberry"

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("uni")

driver.find_element(By.LINK_TEXT, "United States of America").click()
driver.find_element(By.CSS_SELECTOR,'div[class= "checkbox checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
mss = driver.find_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']").text
print(mss)
assert  "Success! Thank you!" in mss
assert driver.find_element(By.ID, "checkbox2").is_selected()

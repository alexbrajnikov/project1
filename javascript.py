import driver as driver
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Alex")
print(driver.execute_script("return document.getElementsByName('name')[0].value"))

shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop]")
driver.execute_script("argumets[0].click:",shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

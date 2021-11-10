
from selenium import webdriver
import time

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_element(By.XPATH,"//div[@class='card h-100']")
for product in products:
   product_name = product.find_element(By.XPATH,"div/h4/a").text 
   if product_name == "Blackberry":
   product.find_element(By.XPATH,"//button").click
   
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary'").click()
cart_element= find_element(by.XPATH,"//h4/a[@href='#']").text
assert cart_element =="Blackberry"

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("uni")
webDriverWait(driver,7)
wait.until(expected_conditions.presense_of_element_located((By.LINK_TEXT,"United States of America")))
driver.find_element(By.LINK_TEXT, "United States of America").click()
driver.find_element(By.ID,"checkbox2" ).click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
mss = driver.find_element(By.XPATH, "//*[@class='alert alert-success alert-dismissible']").text
assert mss == "Success! Thank you! Your order will be delivered in next few weeks :-)."
assert driver.find_element(By.ID,"checkbox2" ).is_selected()

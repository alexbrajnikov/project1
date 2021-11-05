from selenium import webdriver
import time


driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("// input[@type="search" ]").send_keys("ber")
time.slep(5)
products = driver.find_element_by_xpath("//div[@class='products']/div")
count = len(products)
assert count == 3
buttons = find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()
    
driver.find_elements_by_xpath("//a[@class='cart-icon']").click()
driver.find_elements_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element_by_cssselector("input.promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_cssselector("button.promoBtn").click()
mss=driver.find_element_by_cssselector(".promoInfo").text
assert 'applied' in mss

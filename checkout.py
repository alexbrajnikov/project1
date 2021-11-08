
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicit_wait(20)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("// input[@type="search" ]").send_keys("ber")
time.slep(5)
products = driver.find_element_by_xpath("//div[@class='products']/div")
count = len(products)
assert count == 3
buttons = find_elements_by_xpath("//div[@class='product-action']/button")
cart = []
for button in buttons:
    cart.append(button.find_elements_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(cart)
list = []    
driver.find_elements_by_xpath("//a[@class='cart-icon']").click()
driver.find_elements_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()
items=driver.find_elements_by_css_selector("p.product-name")
for item in items:
    list.append(item.text)
print(list)

assert cart == list
driver.find_element_by_css_selector("input.promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector("button.promoBtn").click()
mss=driver.find_element_by_css_selector(".promoInfo").text
assert 'applied' in mss

after_discount = driver.find_element_by_css_selector("span.discountAmt").text
total = driver.find_element_by_css_selector("span.totAmt").text
assert float(after_discount) == float(total - (total*0.1))

amounts = find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
    
assert int(total) == sum

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath('https://rahulshettyacademy.com/AutomationPractice/')

print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert checkbox.is_selected()

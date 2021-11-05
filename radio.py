from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath('//*[@name="radioButton"]')

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()   
    
radiobuttons = driver.find_elements_by_xpath("//*[@name='radioButton']")
radiobuttons[2].click()
assert radiobuttons[2].is_selected

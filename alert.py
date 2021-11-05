from selenium import webdriver
import time

validatetext = "Option3"
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(validatetext)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
if validatetext in alert.text:
    assert
    alert.accept()

name = "Alex"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element_by_cssselector("#confirmbtn")
alert = driver.switch_to.alert
text = alert.text
assert name in text
alert.dissmiss()

from selenium import webdriver
import time
from selenium.webdriver.common.by imports By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
select = Select(driver.find_element(By.XPATH, "//button[text()='Customer Login']"))
select.select_by_value("2")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

balance= driver.find_element(By.XPATH, "//div[@class= 'center'][1]/strong[2]").text

print(balance)

driver.find_element(By.CSS_SELECTOR, "button[ng-class='btnClass2']").click()
driver.find_driver.find_element(By.CSS_SELECTOR, "driver.find_element(By.CSS_SELECTOR, "input[type='number']").click()
driver.find_driver.find_element(By.CSS_SELECTOR, "driver.find_element(By.CSS_SELECTOR, "input[type='number']").send_keys("10000")
driver.find_driver.find_element(By.CSS_SELECTOR, "driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

balance_after_dep= driver.find_element(By.XPATH, "//div[@class= 'center'][1]/strong[2]").text

print(balance_after_dep)

assert (int(balance) +10000) == int(balance_after_dep)

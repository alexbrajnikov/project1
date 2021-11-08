from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate")
driver.switch_to.default_content()

print(driver.find_element(By.TAG_NAME, "h3"))

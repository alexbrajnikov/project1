from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH, "//div[@class='example']/a").click()
window = driver.window_handles
driver.switch_to.window(window[1])
print(driver.get_element(By.TAG_NAME, "h3"))
driver.switch_to.window(window[0])
print(driver.get_element(By.TAG_NAME, "h3"))

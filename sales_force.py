from selenium import webdriver

driver=webdriver.Chrome(executable_path="C\\chromedriver.exe")

driver.get('https://login.salesforce.com/')
driver.find_element_by_css_selector("#username").send_keys("Alex")
driver.find_element_by_css_selector(".password").send_keys("1234")
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']).click()

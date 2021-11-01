from Selenium import webdriver

driver=webdriver.Chrome(executable_path="C\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Alex")
driver.find_element_by_name("email").send_keys("Alex@gmail.com")
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys('1234')
driver.find_element_by_css_selector(input(id="exampleCheck1")).click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1")
dropdown.select_by_index(0)



driver.find_element_by_xpath("input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text()
assert "success" in message

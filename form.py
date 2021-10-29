from Selenium import webdriver

driver=webdriver.Chrome(executable_path="C\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Alex")
driver.find_element_by_name("email").send_keys("Alex@gmail.com")
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys('1234')
driver.find_element_by_css_selector(input(id="exampleCheck1")).click()



driver.find_element_by_css_selector(input(type='submit')).click()

text=driver.find_element_by_class_name("alert-success").text()
if text="Success! The Form has been submitted successfully!.":
    print("Pass")
else:
    print("Failed")
    

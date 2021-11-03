from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys('uzb')
time.sleep(2)
countries = driver.find_elements_by_sccselector("li[class=ui-menu-item'] a")
for country in countries:
    if coutry.text == "Uzbekistan":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == 'Uzbekistan'

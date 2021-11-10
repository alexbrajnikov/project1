import driver as driver
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://rahulshettyacademy.com/angularpractice/")

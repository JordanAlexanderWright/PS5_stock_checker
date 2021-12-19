from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome("./chromedriver.exe")

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

buttons = chrome_browser.find_elements_by_class_name("btn-default")

message_form = chrome_browser.find_element_by_id("user-message")
message_form.send_keys("Hello World")
message_button = buttons[0]
message_button.click()

sum_form_a = chrome_browser.find_element_by_id("sum1")
sum_form_b = chrome_browser.find_element_by_id("sum2")
sum_form_a.send_keys("10")
sum_form_b.send_keys("20")

total_button = buttons[1]
total_button.click()

chrome_browser.close()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')
driver.maximize_window()

sleep(1)
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

assert 'Sign-In' in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small' and contains(text(), 'Sign-In')]").text
driver.quit()

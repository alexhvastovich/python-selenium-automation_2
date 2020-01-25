from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')
driver.maximize_window()

#Click help
driver.find_element(By.XPATH, "//a[text()='Customer Service']").click()
sleep(1)

#Cancel order
driver.find_element(By.XPATH, "//input[@id='helpsearch']").send_keys('cancel order')
sleep(1)

driver.find_element(By.XPATH, "//input[@aria-labelledby='helpSearchSubmit-announce']").click()
sleep(1)

#$x("//div[@class='help-content']/h1")
assert driver.page_source.find("Cancel Items or Orders")
sleep(1)

driver.quit()

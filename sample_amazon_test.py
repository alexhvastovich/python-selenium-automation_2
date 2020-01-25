from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_button = driver.find_element(By.XPATH, "//input[@value='Go'][@class='nav-input']")

search.clear()
search.send_keys('Lego')

search_button.click()

#assert
assert 'Lego' in driver.find_element(By.XPATH, "//div[@id='search']//div[@class='a-section a-spacing-small a-spacing-top-small']//span[@class='a-color-state a-text-bold']").text

driver.quit()
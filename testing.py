# Naeem Akhtar demo project for selenium testing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

# open website
driver.get("https://www.python.org")


# exit the browser
driver.quit()
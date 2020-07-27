# Naeem Akhtar demo project for selenium testing
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

# getting title of webpage
def get_title():
	print('title of website: ', driver.title)
	time.sleep(1)


def google_search():
	# search for facebook
	link = 'https://www.google.com'
	driver.get(link)

	get_title()

	search_box = driver.find_element_by_name("q")
	search_box.clear()
	search_box.send_keys('facebook')
	search_box.send_keys(Keys.RETURN)

	time.sleep(1)


# login using credential
def fb_login():
	link = 'https://www.facebook.com'
	driver.get(link)

	get_title()

	username = input('Enter username / email :')
	password = input('Enter password :')

	username_input = driver.find_element_by_id('email')
	username_input.send_keys(username)

	password_input = driver.find_element_by_id('pass')
	password_input.send_keys(password)

	driver.find_element_by_id('loginbutton').click()

	time.sleep(1)


# def navigate_fb():
# 	navigation_bar =  driver.find_element_by_xpath()
# 	print(navigation_bar)

# hamburger menu
# ham_button = driver.find_element_by_id('guide-button')
# ham_button

# testing search bar
# search_bar = driver.find_element_by_id("search-input")
# search_bar.send_keys("Python testing")
# search_bar.send_keys(Keys.RETURN)

google_search()
fb_login()
# navigate_fb()


# exit the browser
# driver.quit()
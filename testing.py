# Naeem Akhtar demo project for selenium testing
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

# getting title of webpage
def get_title():
	print('title of website: ', driver.title)
	time.sleep(1)

# google search bar using find_by_name
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


# login using credential using find_by_id
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


# scroll down and up
def scroll_down_up():
	last_height = driver.execute_script("return document.documentElement.scrollHeight")
	while True:
		# Scroll down
		driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
		# Wait to load page
		time.sleep(1)
		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.documentElement.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
	time.sleep(3)
	# scroll up
	driver.execute_script("window.scrollTo(0,0);")


# facebook search using find_by_xpath
def fb_search(keywords):
	search = driver.find_element_by_xpath("//input[@type='search']")
	search.clear()
	search.send_keys(keywords)
	driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.RETURN)
	time.sleep(1)


# def navigate_fb():
# 	navigation_bar =  driver.find_element_by_xpath()
# 	print(navigation_bar)


google_search()
fb_login()
fb_search('Coronavirus')
scroll_down_up()
# navigate_fb()


# exit the browser
time.sleep(3)
driver.quit()
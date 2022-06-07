from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import data_file

url = data_file.url
username = data_file.username
password = data_file.password

browser = webdriver.Firefox()
browser.get(url)
userElem = browser.find_element_by_name('username')
userElem.send_keys(username)

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(password)
passwordElem.send_keys(Keys.RETURN)

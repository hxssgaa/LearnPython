# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


# driver = webdriver.PhantomJS(executable_path='/Users/hxssg/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver = webdriver.Chrome(executable_path='/Users/hxssg/Downloads/chromedriver')
print 'webdriver initialization complete....'
driver.get("http://bbs.feng.com")
print driver.title

elems = driver.find_elements_by_link_text("登录")
elem = elems[-1]
elem.click()
print driver.title

user_element = driver.find_element_by_xpath("//input[@name='username']")
pass_element = driver.find_element_by_xpath("//input[@name='password']")
user_element.send_keys('hxssgaa')
pass_element.send_keys('6867138811')

ok_button = driver.find_element_by_xpath("//button[@class='btn ok_btn']")
ok_button.click()

print driver.page_source

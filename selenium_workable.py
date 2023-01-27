from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')
sleep(5)
browser.close()

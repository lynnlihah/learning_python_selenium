# coding = utf-8

from selenium import webdriver
import time

# browser = webdriver.Firefox() - 报错
browser = webdriver.Chrome()

browser.get('http://www.baidu.com')
time.sleep(0.3)
print(browser.title)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()

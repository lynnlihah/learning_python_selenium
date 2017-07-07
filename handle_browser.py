#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://www.baidu.com"

print("now access %s" % url)
browser.get(url)

time.sleep(2)

# 将浏览器最大化 - 报错
# browser.maximize_window()
# time.sleep(3)

# 设置浏览器固定宽高 - 报错
# browser.set_window_size(480, 800)
# time.sleep(3)

# 前进后退
s_url = "http://news.baidu.com"
browser.get(s_url)
time.sleep(2)

browser.back()
time.sleep(1)

browser.refresh()
time.sleep(1)

browser.forward()
time.sleep(2)

browser.quit()
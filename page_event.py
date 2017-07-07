#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 点击和输入/提交/返回元素信息等
from selenium import webdriver
import time

driver =  webdriver.Chrome()
driver.get("http://www.baidu.com")

# Click
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(1)
driver.find_element_by_id('su').click()

# submit 提交表单
search_text = driver.find_element_by_id('kw')
search_text.clear()
search_text.send_keys('selenium2')
search_text.submit()

# 有时候 submit()可以与 click()方法互换来使用，
# submit()同样可以提交一个按钮， 但 submit()的应用范围远不及 click()广泛。


driver.back()
time.sleep(1)
driver.back()
time.sleep(1)

# size： 返回元素的尺寸。
# text： 获取元素的文本。
# get_attribute(name)： 获得属性值。
# is_displayed()： 设置该元素是否用户可见。

size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息 - 未获取成功
text = driver.find_element_by_id("cp").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

time.sleep(1)
driver.quit()
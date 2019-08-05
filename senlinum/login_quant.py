#!/usr/bin/env python3

from selenium import webdriver
import time


driver = webdriver.Chrome()
# 操作这个对象.
# get方式访问百度.
driver.get('https://quant.csc108.com')
time.sleep(10)
# 取ID为txtLoginCode的网页元素(用户名输入元素)
elem_user = driver.find_element_by_id('phone-number')
# 清空输入
elem_user.clear()
# 键入用户名
elem_user.send_keys('17197850401')
# 取ID为txtPwd的网页元素(密码输入元素)
elem_pass = driver.find_element_by_id('password')
# 清空输入
elem_pass.clear()
# 键入密码
elem_pass.send_keys('8023dk0814..')
# 取ID为btnLogin的登录按钮
elem_login = driver.find_element_by_id('btn-confirm')
# 点击登录按钮
elem_login.click()

exit(0)


#driver.quit()
# 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.

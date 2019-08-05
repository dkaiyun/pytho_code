#!/usr/bin/env python3

from selenium import webdriver
import time


driver = webdriver.Chrome()
# 操作这个对象.
# get方式访问百度.
driver.get('https://quant.csc108.com/login')
time.sleep(5)
# 取ID为txtLoginCode的网页元素(用户名输入元素)
driver.find_element_by_xpath('//*[@id="page-register"]/main/div[2]/form[3]/div[2]/input').send_keys('17197850401')


# 取ID为txtPwd的网页元素(密码输入元素)
driver.find_elements_by_xpath('//*[@id="page-register"]/main/div[2]/form[3]/div[4]/input[4]')[0].send_keys("8023dk0814..")

# 取ID为btnLogin的登录按钮
driver.find_elements_by_xpath('//*[@id="page-register"]/main/div[2]/form[3]/div[6]/input')[0].click()

driver.quit()
exit(0)


#driver.quit()
# 使用完, 记得关闭浏览器, 不然chromedriver.exe进程为一直在内存中.

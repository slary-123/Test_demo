# -*- coding: utf-8 -*-
# @Time : 2023/7/17 18:44
# @Author : Huihui.zhu
# @File : login_by_cookie.py
# @Software: PyCharm
# 编写的getcookies.py文件
from selenium import webdriver # 导入webdriver驱动
import time
import json
driver=webdriver.Chrome()
# driver.maximize_window()  # 将窗口最大化
# driver.get('https://www.baidu.com') # 访问百度网站
# time.sleep(60) # 等待一段时间，该时间内手动操作登录网站
# # 将cookie保存为json格式，此时会发现当前目录中多了一个cookies.txt的文件
# with open('cookies.txt','w') as f:
#     f.write(json.dumps(driver.get_cookies()))
# driver.quit() # 退出网站


# 编写的addcookies.py文件
from selenium import webdriver # 导入webdriver驱动
import time
import json

driver.maximize_window()  # 将窗口最大化
driver.get('https://www.baidu.com') # 访问百度网站

driver.delete_all_cookies() # 清除由于浏览器打开已有的cookies

with open('cookies.txt','r') as f:
    cookies_list = json.load(f) # 使用json读取cookie，注意读取的是文件，所以用load而不是loads

    for cookie in cookies_list:
        driver.add_cookie(cookie)

driver.refresh() # 刷新浏览器，刷新后发现网站已经通过cookie登录上了

# -*- coding: utf-8 -*-
# @Time : 2023/7/21 16:21
# @Author : Huihui.zhu
# @File : login_page.py
# @Software: PyCharm
import pyautogui as pg
import os
from pywinauto.application import Application
from common.Base_options import Base_options
from testdata.locators import locator
from time import sleep
from common.my_logger import logger
class Login(Base_options, locator):
    def start_app(self):
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"}) # __COMPAT_LAYER是一个系统环境变量，它允许您设置兼容性图层，这是您右键单击可执行文件时可以调整的设置，选择“属性”，然后转到“兼容性”选项卡。使用__COMPAT_LAYER的
#设置__COMPAT_LAYER到RunAsInvoker 安全实际上并没有给你管理员权限，如果你没有他们;它只是防止出现UAC弹出窗口
        self.app = Application('win32').start(self.Paths.test_app_path)
        logger.info("启动应用程序")
        return self.app
    def login_app(self):

        self.click_loc(self.login_page.feishu,'点击飞书')
        sleep(2)
        pg.scroll(-300) # 向下滚动300C:\Users\user\Desktop\big-house\10000.jpg
        self.click_loc(self.login_page.shouquan,'点击授权')
        sleep(6)

if __name__ == '__main__':
    pass
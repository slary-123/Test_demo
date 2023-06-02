import pyautogui as pg
import os
from pywinauto.application import Application
from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc

class Test_login_page:
    def test_start_app(self):
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
        self.app = Application('win32').start(loc.Paths.apppath)
        print("启动应用程序")
        return self.app
    # def __init__(self):
    #     # 管理员权限打开程序
    #     os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    #     self.app = Application('win32').start(r'D:\工具相关\Launcher\BIMDesigner.exe')

    def test_login(self):
        bo().click_loc(loc.login_page.feishu)
        pg.scroll(-300)
        bo().click_loc(loc.login_page.shouquan)



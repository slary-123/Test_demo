# -*- coding: utf-8 -*-
# @Time : 2023/7/28 9:13
# @Author : Huihui.zhu
# @File : test_create_plan.py
# @Software: PyCharm
from time import sleep
from pageobject.login import Login
from pageobject.create_plan_page import Create_Plan
import pytest
import allure
allure.epic("应用大师方案")
allure.story("识别户型应该方案")
allure.title("应用方案")
def test_aply_plan():
    Login().start_app()
    sleep(2)
    Login().login_app()
    Create_Plan().create_house_plan()
    sleep(3)

if __name__ == '__main__':
    pytest.main(["vs",'-k test',__file__])

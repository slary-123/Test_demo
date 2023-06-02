from time import sleep
from pageobject.login import Login
import pytest
import allure
allure.epic("登陆模块")
allure.story("用户登陆")
allure.title("登陆住小橙客户端并新建项目")
def test_login_page():
    Login().start_app()
    sleep(2)
    Login().login_app()

if __name__ == '__main__':
    pytest.main(["vs",__file__])



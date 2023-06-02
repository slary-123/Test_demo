#coding=utf-8
import time
import pytest,os
if __name__ == '__main__':
  #  pytest.main(['-vs','test_case/test_login_page.py'])
   # pytest.main(['-vs', 'test_case/test_createProject.py'])
    pytest.main(['-vs','test_case/test_index_page_01.py'])
    time.sleep(1)
#    os.system("allure generate reports/temps --clean")
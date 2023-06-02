import Test_demo.test_case.test_index_page_01
from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc
import pyautogui as pg
import os,time
class  Test_fangan_page(Test_demo.test_case.test_index_page_01):
    def test_fangan(self):
        bo().move(loc.index_page.tu)
        bo().click_loc(loc.index_page.yingyong)
        bo().click_loc(loc.index_page.yijianyingyong)
        time.sleep(15)
        bo().click_loc(loc.index_page.dimian)
        bo().click_loc(loc.index_page.dimzhidaoleian)
        shotfile = os.path.join(loc.index_page.screenshotpath,'test.png')
        pg.screenshot(shotfile)
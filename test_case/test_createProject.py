from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc
import pyautogui as pg
import os,time
class Test_createProject:
    def test_createProject(self):
        bo().click_loc(loc.index_page.xinjian)
        bo().click_loc(loc.index_page.ziyouhuizhi)
        while True:
            try:
                time.sleep(1)
                loc1 = bo.get_path(loc.index_page.huxing)
                a = pg.locateOnScreen(loc1)  # 查找该图像，并返回其位置信息
                x, y = pg.center(a)  # 获取该图像位置的中心点坐标
                print("进入原始户型", x, y)
                break
            except TypeError:
                print('加载中...')
                continue
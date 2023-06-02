# -*- coding: utf-8 -*-
# @Time : 2023/7/21 17:07
# @Author : Huihui.zhu
# @File : loc_x_y.py
# @Software: PyCharm
from openpyxl.drawing.image import Image
from common.Base_options import Base_options as bo
from testdata.locators import locator as loc
from common.my_logger import logger
import pyautogui as pg
from time import sleep
def get_position(num):
    '''
    获取鼠标坐标小工具
    :param times:
    :return:
    '''
    for i in range(num):
        logger.info(f"当前鼠标位置坐标：{pg.position()}")
        sleep(2)

get_position(50)

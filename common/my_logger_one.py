# -*- coding: utf-8 -*-
# @Time : 2023/7/21 19:29
# @Author : Huihui.zhu
import logging
from configparser import ConfigParser
from loguru import logger
from time import strftime
from util.handle_path import Log_Path
from logging import getLogger
class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)
class MyLog(logging.Logger):
    __instance = None  # 单例实现
    __call_flag = True  # 如果调用过就不再调用
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,name,level=logging.INFO,file=None):
        super().__init__(name,level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s- %(lineno)d行----- %(message)s')
        if self.__call_flag:
         # 控制台输出
            handle1 = logging.StreamHandler()
            handle1.setFormatter(formatter)
            self.addHandler(handle1)
        # 输出在文件
        if file:
            handle2 = logging.FileHandler(file,encoding='utf-8')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
if __name__ == '__main__':
    logger = MyLog('zxc',"INFO",r"C:\Users\user\Desktop\log.txt")
    logger.info("hahhahahahaaa")
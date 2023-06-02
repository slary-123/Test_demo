#
# # -*- coding: utf-8 -*-
# # @Time : 2023/7/21 19:29
# # @Author : Huihui.zhu
# import logging
# from configparser import ConfigParser
# from loguru import logger
# from time import strftime
# from util.handle_path import Log_Path
# from logging import getLogger
# class PropogateHandler(logging.Handler):
#     def emit(self, record):
#         logging.getLogger(record.name).handle(record)
# class MyLog():
#     __instance = None  # 单例实现
#     __call_flag = True  # 如果调用过就不再调用
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#     def get_log(self):
#         if self.__call_flag:
#             #输出在文件，级别设置为error
#             curdate = strftime('%Y%m%d_%H%M%S')
#             cfg = ConfigParser()  # 标准库ConfigParser读取ini文件
#             cfg.read(Log_Path.config_path / 'loguru.ini', encoding='utf-8') # D:\pycharm\Test_demo\outfiles\log
#             # logger.remove(handler_id=None)   # 关闭console输出
#             logger.add(Log_Path.log_path / f'zxc_{curdate}.log',  # 日志存放位置
#                        retention=cfg.get('log', 'retention'),
#                        rotation=cfg.get('log', 'rotation'),
#                        format=cfg.get('log', 'format'),
#                        compression='zip',  # 日志压缩格式
#                        level=cfg.get('log', 'level'))  # 日志级别
#
#             # 将日志输出到console控制台，级别设为info
#             console_handler = logging.StreamHandler()
#             console_handler.setLevel(logging.INFO)  # 设置日志级别为INFO或其他您需要的级别
#             formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#             console_handler.setFormatter(formatter)
#             logger.add(console_handler)
#             self.__call_flag = False  # 调用过就置为False
#         return logger
# log = MyLog().get_log()
# if __name__ == '__main__':
#     log = MyLog().get_log()
#     def div_calcul():
#         try:
#             result = 5 / 0
#             print(result)
#             logger.info("输出结果成功")
#         except Exception as e:
#             logger.debug("[计算出错原因为：%s]" % e)
#     div_calcul() #执行该方法，预期会报错

#=======================new=========================
import logging
class MyLogger(logging.Logger):
    def  __init__(self,__name__,level=logging.INFO,file=None):
        super().__init__(__name__,level)
        #日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行： %(message)s'
        formatter = logging.Formatter(fmt)

        #控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            #文件渠道
            handle2 = logging.FileHandler(file, encoding='utf-8')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
logger=MyLogger(__name__)
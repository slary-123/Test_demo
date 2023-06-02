import pyautogui
import pyautogui as pg
import time,os
from pywinauto.application import Application
#x, y = pg.position()
from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc
import pyautogui as pg
import os,time
# # # 当前鼠标位置：x=838, y=689
# #print("当前鼠标位置：x={}, y={}".format(x, y)
# # os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
# # app = Application("win32").start(r'D:\工具相关\Launcher\BIMDesigner.exe')
# # time.sleep(2)
# # pg.moveTo(x=1105,y=700)
# # time.sleep(2)
# # pg.click()
# # pg.click()
# # time.sleep(2)
# # pg.scroll(-300)
# # pg.click(x=1209,y=873)
# # # pg.doubleClick()
# #time.sleep(2)
# #pyautogui.click(x=1231, y=435)
#
# class test:
#     def upload(self, path, filename, name):
#         bo().move(loc.index_page.huxing)
#         bo().click_loc(loc.index_page.daorutupian)
#         if bo().get_loc(loc.index_page.queren):
#             bo().click_loc(loc.index_page.queren)
#         file = os.path.join(loc.index_page.path, filename)
#         bo().upload(file)  # 调用上传图片
#         faillist = []
#         # 使用 `os.walk()` 方法遍历目录树，返回三个值：P:当前目录路径、m:当前目录下的子目录列表、当前目录下的文件列表。
#         for p, m, names in os.walk(loc.index_page.path):
#             print('---户型图总数：', len(names))
#             for name in names:
#                 print('---户型id：', name[:-4])
#                 try:
#                     # path:上传图片路径、   name：图片名称
#                     test().upload(path=loc.index_page.path, filename=name, name=name[:-4])
#                     print(f"{name[:-4]} 执行成功！")
#                 except Exception:
#                     print(f"{name[:-4]} 执行失败了！")
#                     faillist.append(name[:-5])
#         print('执行完毕')
# if __name__ == '__main__':
#     test().upload(loc.index_page.path,'HomeThumbnail_1655652889630.jpg','HomeThumbnail_1655652889630')
#

class test:
        def upload(self):
            bo().move(loc.index_page.huxing)
            bo().click_loc(loc.index_page.daorutupian)
            # if bo().get_loc(loc.index_page.queren):
            #     bo().click_loc(loc.index_page.queren)
            faillist = []
            # 使用 `os.walk()` 方法遍历目录树，返回三个值：P:当前目录路径、m:当前目录下的子目录列表、当前目录下的文件列表。
            for p, m, names in os.walk(loc.index_page.path):
                print("当前目录路径:",p)
                print("当前目录下的文件列表:", names)
                print('---户型图总数：', len(names))
                for name in names:
                    print('---户型id：', name[:-4])
                    try:
                        # path:上传图片路径、   name：图片名称
                      #  test().upload(path=loc.index_page.path, filename=name, name=name[:-4])
                        file = os.path.join(loc.index_page.path,name)
                        print("上传图片路径:",file)
                        bo().upload(file)  # 调用上传图片
                        print(f"{name[:-4]} 执行成功！")
                    except Exception:
                        print(f"{name[:-4]} 执行失败了！")
                        faillist.append(name[:-5])
            print('执行完毕')
if __name__ == '__main__':

    test().upload()
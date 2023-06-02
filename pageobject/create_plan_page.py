# -*- coding: utf-8 -*-
# @Time : 2023/7/28 9:18
# @Author : Huihui.zhu
# @File : create_plan_page.py
# @Software: PyCharm
import pyautogui
from common.Base_options import Base_options
from testdata.locators import locator
from time import sleep
from common.my_logger import logger
import os,pyperclip,openpyxl
class Create_Plan(Base_options,locator):
    def dict_plan_name(self,file_path):  # 将图片地址和方案名称写入字典里面
        plan_img = {} # 定义一个空字典
        plan_name = ['北欧-质雅温润','现代黑白灰', '日式-原木风','中式-简洁端庄']
        house_file_path = self.get_pic_to_list(file_path)
        for i in range(len(house_file_path)):
            plan_img[house_file_path[i]] = plan_name[i % len(plan_name)]
        logger.info("图片地址-大师方案:",plan_img)
        return plan_img
    def create_house_plan(self): # 进入户型图导入界面
        file_dict = self.dict_plan_name(self.index_page.path)
        logger.info('打印字典：',file_dict)
        while True:
            for house_path,plan_name in file_dict.items(): # 遍历列表
                print('=============================第一阶段：新建项目+自由绘制导入图片+自动识别=============================')
                if self.get_loc(self.index_page.new_project,'获取新建项目元素'):
                    sleep(3)
                    self.move(self.index_page.new_project,'鼠标移动到新建项目')
                    sleep(1)
                    self.click_loc(self.index_page.new_project,'鼠标点击新建项目')
                    sleep(6)
                if self.get_loc(self.index_page.free_draw,'获取自由绘制'):
                    self.click_loc(self.index_page.free_draw,'点击自由绘制')
                    sleep(3)
                    if self.get_loc(self.index_page.house_size,'获取户型图片'):
                        sleep(2)
                        self.move(self.index_page.house_size,'获取户型图片的坐标并将鼠标移动到户型坐标上')  # 鼠标悬浮在户型图标上
                        sleep(2)
                        self.click_loc(self.index_page.upload_house_img,'点击导入图片')
                        sleep(2)
                        self.upload(house_path,'上传户型图片')  # 上传户型图片
                        sleep(5)
                        self.click_loc(self.index_page.auto_recongize,'点击自动识别')
                        sleep(10)
                print('=============================第二阶段：新建方案+继续新建方案=============================')
                if self.get_loc(self.index_page.index_new_plan,'高亮的新建方案'):
                    print(f"{house_path}户型识别成功!")
                    self.click(1860,64)
                    self.click(1860,64)
                    sleep(4)
                    for i in range(2):
                        if  self.get_loc(self.index_page.pre_continue_create):
                            sleep(1)
                            self.click(1113,780)
                            sleep(1)
                            self.click_loc(self.index_page.continue_create)
                            sleep(5)
                        else:
                            continue
                print('=============================第三阶段：搜索大师方案+下载或者应用方案=============================')
                if self.get_loc(self.index_page.plan_name_input,'获取方案名称输入框'):
                    sleep(2)
                    for i in range(2):
                        self.click_loc(self.index_page.plan_name_input,'双击方案名称输入框')
                        sleep(1)
                    pyperclip.copy(plan_name)    # 将大师方案名称复制到剪贴板
                    pyautogui.hotkey('ctrl','v') # 将案例名称粘贴在输入框中
                    pyautogui.press('enter')     # 点击enter进行搜索
                    sleep(2)
                    pyautogui.moveTo(x=241, y=380)  # 鼠标移动至大师方案图片上
                    sleep(2)
                    if not self.get_loc(self.index_page.aply_plan,'点击应用按钮'): # 如果点击获取不到应用按钮则方案可能未被下载
                        sleep(2)
                        self.click_loc(self.index_page.download_plan,'点击下载大师方案')
                        sleep(10)
                    if self.get_loc(self.index_page.aply_plan,'获取应用大师方案按钮'):
                        sleep(2)
                        self.click_loc(self.index_page.aply_plan,'点击应用大师方案按钮')
                        sleep(5)
                print('=============================第四阶段：继续应用大师方案+保存并退出方案=============================')
                if self.get_loc(self.index_page.auto_aply,'获取一键应用按钮'):
                    sleep(3)
                    self.move(self.index_page.auto_aply, '点击一键应用按钮')
                    sleep(1)
                    self.click_loc(self.index_page.auto_aply,'点击一键应用按钮')
                    sleep(24)
                    print('=============================第五阶段：点击【知道了】+保存并退出方案=============================')
                    if not self.get_loc(self.index_page.know,'获取知道了按钮'):
                        print("方案正在应用中，请稍等..........")
                        sleep(6)
                        self.click(1892, 16)
                        sleep(3)
                        self.click_loc(self.index_page.save_exit, '点击保存并退出按钮')
                        sleep(10)
                    if self.get_loc(self.index_page.know, '获取知道了按钮'):
                        self.click_loc(self.index_page.know,'点击知道了')
                        sleep(7)
                        if self.get_loc(self.index_page.exit,'获取退出按钮定位'):
                            sleep(3)
                            self.click(1892,16)
                            sleep(3)
                            self.click_loc(self.index_page.save_exit,'点击保存并退出按钮')
                            sleep(10)
                continue

if __name__ == '__main__':
     house = Create_Plan()
     house.dict_plan_name(r"C:\Users\user\Desktop\house_file")
     sleep(3)











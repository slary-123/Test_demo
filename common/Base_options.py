'''
pyautogui基础操作封装
'''
import pyautogui as pg
import time, os
class Base_options:

    def __init__(self):
        time.sleep(3)

    # 基础操作封装
    def click(self, x, y):
        time.sleep(3)
        pg.click(x, y)
        print("获取坐标",x,y)
        time.sleep(3)

    def doubleClick(self, x, y):
        time.sleep(2)
        pg.doubleClick(x, y)
        time.sleep(2)
        pg.doubleClick(x, y)

    def mouseClick(self, x, y):
        time.sleep(3)
        pg.mouseDown(x=x, y=y)
        time.sleep(3)
        pg.mouseUp(x=x, y=y)

    @staticmethod
    def get_path(image): #获取图像文件的路径
        image_path = r"C:\Users\User\Desktop\loc_image"
        path = os.path.join(image_path,image)
        print(f'图片路径{path}')
        return path

    def get_loc(self,image):
        try:
            png=Base_options.get_path(image)
            print("图片路径2：",png)
            a=pg.locateOnScreen(png) #查找该图像，并返回其位置信息
            print(f'图像位置:{a}')
            x,y=pg.center(a) #获取该图像位置的中心点坐标
            print(f'图片中心点坐标:{image},x={x},y={y}')
            return x,y
        except Exception:
            print(f"图片识别失败:{image}")
            return False

    def click_loc(self, image):
        for i in range(3):
            try:
                x, y = self.get_loc(image) #调用get_loc方法获取图像位置中心坐标
                self.click(x, y)#点击坐标
                print(f'点击坐标:x:{x},y{y}')
                return
            except TypeError:
                time.sleep(3)
                print(f'{image}点击操作失败，等待第{i + 1}重试！')
                continue
            else:
                print("========================执行成功===========================")
            finally:
                print("=========================单次点击结束================================")

    def doubleClick_loc(self, image):
        for i in range(3):
            try:
                x, y = self.get_loc(image) #调用get_loc方法获取图像位置中心坐标
                time.sleep(1)
                self.doubleClick(x, y)#点击坐标
                print(f'双击坐标:x:{x},y{y}')
                return
            except TypeError:
                time.sleep(3)
                print(f'{image}点击操作失败，等待第{i + 1}重试！')
                continue
            else:
                print("========================执行成功===========================")
            finally:
                print("=========================结束================================")

    def mouseClick_loc(self, image):
        for i in range(3):
            try:
                x, y = self.get_loc(image) #调用get_loc方法获取图像位置中心坐标
                time.sleep(1)
                #self.mouseClick(x, y)#点击坐标
                print(f'双击坐标:x:{x},y{y}')
                return
            except TypeError:
                time.sleep(3)
                print(f'{image}点击操作失败，等待第{i + 1}重试！')
                continue
            else:
                print("========================执行成功===========================")
            finally:
                print("=========================结束================================")


    def move(self, image):
        time.sleep(3)
        for i in range(3):
            try:
                x, y = self.get_loc(image)
                pg.moveTo(x, y) #将鼠标移动至对应的坐标
                print("移动坐标：",x, y)
                # time.sleep(3)
                # pg.click(clicks=5,interval=0.5)
                # print("====第一次点击====")
                # time.sleep(3)
                # pg.leftClick(x=x, y=y)
                # print("====第二次点击====")
                # time.sleep(3)
                # pg.mouseDown(x=x, y=y)
                # print("====第三次点击====")
                # time.sleep(3)
                # pg.mouseUp(x=x, y=y)
                # print("====第三次抬起====")
                # pg.click()
                # print("====第四次点击====")
                # pg.doubleClick()
                # pg.doubleClick()
                # pg.doubleClick()

                break
            except Exception:
                continue

    def upload(self, file):
        print(f'---上传图片：{file}')
        pg.typewrite(file) #将文件名输入到当前焦点所在的文本框中
        pg.hotkey('enter')
        time.sleep(1)
        pg.hotkey('enter') #模拟按下回车键，完成上传操作。

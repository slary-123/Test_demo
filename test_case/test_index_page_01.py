from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc
import pyautogui as pg
import os,time

class  Test_index_page:
    def test_upload(self):
        bo().move(loc.index_page.huxing)
        bo().click_loc(loc.index_page.daorutupian)
        faillist = []
        # 使用 `os.walk()` 方法遍历目录树，返回三个值：P:当前目录路径、m:当前目录下的子目录列表、当前目录下的文件列表。
        for p, m, names in os.walk(loc.index_page.path):
            print("当前目录路径:",p)
            print("当前目录下的文件列表:", names)
            print('---户型图总数：', len(names))
            for name in names:
                print('---户型id：', name[:-4])
                try:
                    file = os.path.join(loc.index_page.path,name)
                    print("上传图片路径:",file)
                    bo().upload(file)  # 调用上传图片
                    while 1:
                        try:
                            time.sleep(1)
                            bo().click(x=1256, y=895)
                            break
                        except TypeError:
                            print('户型图上传中...')
                            continue

                    while True:
                        try:
                            time.sleep(1)
                            time.sleep(0.5)
                            pg.moveTo(x=365, y=84)
                            time.sleep(5)
                            shotfile = os.path.join(loc.index_page.screenshotpath, f"{name}j.png")
                            pg.screenshot(shotfile)  # 截图保存到shotfile文件路径中
                            print(f"-----{name} 截图完成")
                            break
                        except TypeError:
                            print('户型生成中...')
                            continue
                    print(f"{name[:-4]} 执行成功！")
                    time.sleep(2)
                    try:
                        bo().click_loc(loc.index_page.xin_fang)
                        bo().click_loc(loc.index_page.jixuxinjianfangan)

                    except:
                        bo().click_loc(loc.index_page.x)
                        bo().click_loc(loc.index_page.bao_tui)
                        bo().click_loc(loc.index_page.xinjianfangan)
                    bo().move(loc.index_page.tu)
                    bo().click_loc(loc.index_page.yingyong)
                    bo().click_loc(loc.index_page.yijianyingyong)
                    time.sleep(15)
                    bo().click_loc(loc.index_page.dimian)
                    bo().click_loc(loc.index_page.zhidaole)
                    shotfile = os.path.join(loc.index_page.screenshotpath, 'test.png')
                    pg.screenshot(shotfile)
                except Exception:
                    print(f"{name[:-4]} 执行失败了！")
                    faillist.append(name[:-5])
        print('执行完毕')
from Test_demo.common.Base_options import Base_options as bo
from Test_demo.data.locators import locators as loc
import pyautogui as pg
import os, time
shotfile = os.path.join(loc.index_page.screenshotpath,'test.png')
print(shotfile)
try:

    bo().click_loc(loc.index_page.xin_fang)
    bo().click_loc(loc.index_page.jixuxinjianfangan)

except:
    bo().click_loc(loc.index_page.x)
    bo().click_loc(loc.index_page.bao_tui)
    bo().click_loc(loc.index_page.xinjianfangan)
# for ii in range(5):
#     if bo().get_loc(loc.index_page.queren):
#         bo().click_loc(loc.index_page.queren)
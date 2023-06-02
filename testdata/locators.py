'''
    所有地址放在Paths中
    所有定位图片及定位坐标集合：根据page分类
    '''
class locator:
    class Paths:
        test_app_path = r'C:\Program Files (x86)\BNQ\BNQ_Bim_Inner_Test_2.0\Launcher\BIMDesigner.exe'  # 测试环境住小橙可执行文件地址
        screenshotpath = r'..\auto_houstscreenshot'            # 测试环境截图的地址
        app_path_zheng = r'D:\online\Launcher\BIMDesigner.exe' # 正式环境住小橙可执行地址
        screenshotpath_zheng = r'..\auto_houstscreenshot'      # 正式环境截图的地址
    class login_page: # 登陆页面
        feishui_x=1105
        feishui_y = 700
        shouquan_x = 1209
        shouquan_y = 873
        feishu = 'feishu.png'
        shouquan = 'shouquan.png'
    class index_page: # 首页页面开始往后所有的页面
        path = r"C:\Users\user\Desktop\house_file" #户型图文件夹路径
        new_project = 'new_project.png' # 新建项目图片
        free_draw = 'free_draw.png'  # 自由绘制
        house_size = 'huxing.png' # 户型图片
        screen_path = r'C:\Users\user\Desktop\screenshot'  # 截图上传路径
        upload_house_img = 'upload_house_img.png' # 导入户型图片
        auto_recongize='auto_recogize.png'
        queren = 'queren.png' # 确认按钮
        quxiao='quxiao.png' # 取消按钮
        index_new_plan='index_new_plan.png' # 首页新建方案
        pre_continue_create = "pre_countiue_create.png"
        continue_create = 'continue_create.png' # 继续新建方案
        plan_save = 'plan_save.png' # 保存方案按钮
        plan_name_input = 'plan_name_input.png' # 方案名称输入框
        aply_plan = 'aply_plan.png' # 应用方案按钮
        download_plan = 'download_plan.png' # 下载方案
        gray_new_plan = 'gray_new_plan.png' # 灰色不可点击的新建方案
        auto_aply = 'auto_aply.png' # 一键应用按钮
        heilight_save = 'heilight_save.png' # 点击高亮保存按钮
        exit = 'exit.png' # 点击退出按钮
        save_exit = 'save_exit.png' # 点击保存并退出按钮
        know = "know.png" # 知道了
        # yingyong='yingyong.png'
        # yijianyingyong='yijianyingyong.png'
        # dimian='dimian.png'
        # dingmian='dingmian.png'
        # manyou='manyou.png'
        # daochu='daochu.png'
        # zhidaole='zhidaole.png'
        # zheng_quan='zheng_quan.png'
        # shengcheng='shengcheng.png'
        # quanjingtu_ok='quanjingtu_ok.png'
        # quan_jing_tu='quan_jing_tu.png'
        # sheng_cheng_zheng='sheng_cheng_zheng.png'
        # fuzhi='fuzhi.png'
        # baocun_tuichu='baocun_tuichu.png'
        # xiangmu_list='xiangmu_list.png'
        # limian_moshi='limian_moshi.png'
        # shihui_moxing='shihui_moxing.png'
        # baocun='baocun.png'
        # xiangmu_guanli='xiangmu_guanli.png'
        # anli_name='anli_name.png'
        # xingmu_list='xingmu_list.png'
        # dakai="dakai.png"
        # xinjianwenjianjia='xinjianwenjianjia.png'
        # weimingming='weimingming.png'
        # weimingmingfangan='weimingmingfangan.png'
        # yinngyzhidaole='yinngyzhidaole.png'
        # quxiao_01='quxiao_01.png'
        # tixing='tixing.png'
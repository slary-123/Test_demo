# -*- coding: utf-8 -*-
# @Time : 2023/7/21 18:01
# @Author : Huihui.zhu
# @File : handle_path.py
# @Software: PyCharm
from pathlib import Path
import collections
collections.Hashable = collections.abc.Hashable
import collections
import collections.abc
from pptx import Presentation
class Log_Path:
    project_path = Path(__file__).parent.parent
    testdata_path = project_path / 'testdata'
    outfiles_path = project_path / 'outfiles'
    report_path = outfiles_path / 'report'
    screenshot_path = outfiles_path / 'screenshot'
    log_path = outfiles_path / 'log'
    config_path = project_path / 'configs'


if __name__ == '__main__':
    print(Log_Path.report_path)
    print(Log_Path.config_path)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 17:44
# @Site    : 
# @File    : report.py
# @Software: PyCharm

import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

class ReportOutput():
    def reportOutput(self,test_dir,report_dir,name_project):
        '''
        :param test_dir: 用例路径
        :param report_dir: 报告路径
        :param name_project: 项目名称=>用于报告命名及描述
        :return:
        '''
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_C2_G_system_Server_config.py")      #加载测试用例
        report_name = report_dir + now + '-'+ name_project+'_test_report.html'    #报告名称
        with open(report_name,'wb') as f:   ##运行用例生成测试报告
            runner = HTMLTestRunner(stream=f,
                                  title=name_project+' UIAuto_Regression Testing Report',
                                  description=(name_project+U"UI自动化功能回归测试"),
                                  verbosity=2)
            runner.run(discover)
            f.close()
import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner


    # 定义测试用例的目录为当前test_case目录
test_dir = './test_code'
suit = unittest.defaultTestLoader.discover(test_dir, pattern="test_C2_J_Wait_ZD.py")


if __name__ == '__main__':
    # 取当前日期时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    html_report = './test_report/' + now_time + 'result.html'
    # html_report='./test_report/result.html'
    with open(html_report, 'wb') as f:#html_report
        runner = HTMLTestRunner(stream=f, title="C2+_财务功能测试报告", description="运行环境："
                                                                 "Windows 10, Chrome浏览器")
        runner.run(suit)
    f.close()

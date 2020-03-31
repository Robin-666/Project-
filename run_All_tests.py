import os
import Log,report


def run():
    pro_name = "2121"
    log_path = os.getcwd()+"\Logs\\"
    print("日志的路径：",log_path)
    report_path = os.getcwd()+"\\test_report\\"
    print( "报告的路径：",report_path)
    testcase_path = os.getcwd()+"\\test_case\服务器配置.xlsx"
    print("用例的路径：",testcase_path)

    logprint = Log.LogOutput()
    logprint.logOutput(log_path,pro_name)

    reportprint = report.ReportOutput()
    reportprint.reportOutput(testcase_path,report_path,pro_name)


if __name__ == '__main__':
    run()

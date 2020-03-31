import logging
import os
from logging.handlers import RotatingFileHandler


class HandleLog:
    """
    处理日志类
    """
    def __init__(self):
        # 创建日志接收器
        self.case = logging.getLogger('case')

        # 定义日志收集器登记
        self.case.setLevel(logging.DEBUG)

        # 定义日志输出渠道
        ss_log = logging.StreamHandler()
        LOGS_DIOR = r'E:\Lexmis_Auto_Object\Lexmis_V71_SP1\C2_CW_NEW\Logs'
        # LOGS_DIOR = '../Logs'
        file_name = RotatingFileHandler(filename=os.path.join(LOGS_DIOR, "cases.log"),
                                        maxBytes=1024,
                                        backupCount=3,
                                        encoding='utf8')

        # 定义日志输出登记
        ss_log.setLevel(logging.ERROR)
        file_name.setLevel(logging.INFO)

        # 定义日志输出格式
        simple_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s")
        # verbose_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(module)s - %(name)s - %(lineno)d - [日志信息]:%(message)s")
        verbose_formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(funcName)s - %(name)s - %(lineno)d - [日志信息]:%(message)s")
        ss_log.setFormatter(simple_formatter)
        file_name.setFormatter(verbose_formatter)

        # 对接，日志收集器与日志输出渠道进行对接
        self.case.addHandler(ss_log)
        self.case.addHandler(file_name)

    def get_logger(self):
        """
        获取logger日志器对象
        :return:
        """

        return self.case

do_log = HandleLog().get_logger()

if __name__ == '__main__':
    do_log.debug("这里是debug日志")
    do_log.info("这里是info日志")
    do_log.warning("这里是warning日志")
    do_log.error("这里是error日志")
    do_log.critical("这里是critical日志")
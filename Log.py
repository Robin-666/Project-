

import time,os
import logging

# print(os.getcwd())

class LogOutput():
    def logOutput(self,log_dir,name_project):
        '''
        :param log_dir: 日志路径
        :param name_project: 项目名称=>用于日志命名
        :return:
        '''
        # sys.path.append(os.chdir('../log'))
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_dir+ now +'-'+name_project+'_test_log.log',
                            filemode='w')
        logger = logging.getLogger()
        logger.info(self)
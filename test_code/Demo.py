import unittest,re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import load_workbook
from selenium.webdriver.support.select import Select

class TestC2_01(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "http://192.168.20.33:8081"
        print("Test Start")

    @classmethod
    def tearDown(cls):
        # cls.driver.quit()
        print("Test End")


    def System_config1(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector("#login_username").send_keys("cxa")  #
        sleep(1)
        self.driver.find_element_by_css_selector("#login_password").send_keys("123456")  # 密码
        sleep(1)
        self.driver.find_element_by_css_selector("#login_button").click()
        self.driver.implicitly_wait(10)  # 等待，直到超出10s还未定位到元素则异常
        self.driver.find_element_by_xpath("//div[@title='财务集成']").click()  # 点击财务集成
        sleep(1)
        ZJM = self.driver.current_window_handle
        sleep(1)
        move = self.driver.find_element_by_xpath("//div[@title='系统配置']")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element_by_xpath("//div[@title='系统配置']").click()
        Win = self.driver.window_handles  # 所有窗口句柄
        for windows in Win:
            if windows != ZJM:
                self.driver.switch_to.window(windows)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(1)
        self.driver.find_element_by_xpath("//div[@title = '服务器配置']").click()
        self.driver.switch_to.frame("myiframe")
        sleep(1)


    # Demo
    def test_a_config(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector("#login_username").send_keys("cxa")  #
        sleep(1)
        self.driver.find_element_by_css_selector("#login_password").send_keys("123456")  # 密码
        sleep(1)
        self.driver.find_element_by_css_selector("#login_button").click()
        self.driver.implicitly_wait(10)  # 等待，直到超出10s还未定位到元素则异常
        self.driver.find_element_by_xpath("//div[@title='财务集成']").click()  # 点击财务集成
        sleep(1)
        ZJM = self.driver.current_window_handle
        sleep(1)
        move = self.driver.find_element_by_xpath("//div[@title='系统配置']")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element_by_xpath("//div[@title='系统配置']").click()
        Win = self.driver.window_handles  # 所有窗口句柄
        for windows in Win:
            if windows != ZJM:
                self.driver.switch_to.window(windows)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(1)
        self.driver.find_element_by_xpath("//div[@title = '服务器配置']").click()
        self.driver.switch_to.frame("myiframe")

        sleep(1)
        self.driver.switch_to.frame("templateSysMgr")
        self.driver.find_element_by_xpath("//div[@class='btnf']/p[1]").click()  # 测试连接
        sleep(1)
        self.driver.switch_to.default_content()
        Msg1 = self.driver.find_element_by_xpath("//div[@class='dialog_main_content_html ']").text
        print(Msg1)  # 当前数据库信息可用!
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//span[@class='right padding_t_10 padding_r_10']/a[1]").click()
        sleep(1)
        self.driver.switch_to.frame("myiframe")
        self.driver.switch_to.frame("templateSysMgr")
        self.driver.find_element_by_xpath("//div[@class='btnf']/p[2]").click()  # 确定
        sleep(1)
        self.driver.switch_to.default_content()
        Msg2 = self.driver.find_element_by_xpath("//div[@class='dialog_main_content_html ']").text
        print(Msg2)  # 服务器数据保存成功!
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//span[@class='right padding_t_10 padding_r_10']/a[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@title = '科目配置']/div/i").click()
        sleep(1)
        self.driver.switch_to.frame("myiframe")
        self.driver.find_element_by_xpath("//select[@id='SubMapping1']").click(  )#
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='SubMapping1']/option[4]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='account1']").click()  #
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='account1']/option[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//a[@id='ClkAdd1']").click(  )  # 新增
        sleep(1)
        Frame1 = "layui-layer-iframe1"
        Frame2 = "layui-layer-iframe2"
        Frame3 = "layui-layer-iframe3"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame1)
        self.driver.find_element_by_xpath("//tr[@id='ConfigTR2']/td/input[2]").click()  # 多级枚举-单位枚举(单位A):
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame2)
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr[1]/td[1]/div/input").click()  # 第一行第一个 一级枚举A
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer2']/div[3]/a[1]").click()  # 确定
        sleep(1)
        self.driver.switch_to.frame(Frame1)
        self.driver.find_element_by_xpath("//tr[@id='FinanceTR']/td/input[2]").click()  # 财务科目:
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame3)
        self.driver.find_element_by_xpath("//span[@id='mytree_2_ico']").click()  # 资产
        sleep(1)
        self.driver.find_element_by_xpath("//div[@class='pDiv']/div/a[4]").click()  # 最后一页
        sleep(1)
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr[2]/td[1]/div/input").click()  # 一级枚举科目
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer3']/div[3]/a[1]").click()  # 确定
        sleep(1)
        self.driver.switch_to.frame(Frame1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='layui-layer-btn layui-layer-btn-']/a[1]").click()  # 保存
        sleep(1)
        self.driver.switch_to.default_content()
        Msg6 = self.driver.find_element_by_xpath("//div[@class='dialog_main_content_html ']").text  #
        print(Msg6)  # 保存成功
        self.driver.find_element_by_xpath("//span[@class='right padding_t_10 padding_r_10']/a[1]").click()  # 确定
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("myiframe")
        sleep(1)
        self.driver.find_element_by_xpath("//a[@id='ClkAdd1']").click()  # 新增
        sleep(1)
        Frame4 = "layui-layer-iframe4"
        Frame5 = "layui-layer-iframe5"
        Frame6 = "layui-layer-iframe6"
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame4)
        self.driver.find_element_by_xpath("//tr[@id='ConfigTR2']/td/input[2]").click()  # 多级枚举-单位枚举(单位A):
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame5)
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr[3]/td[1]/div/input").click()  # 第3个 er级枚举AA
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer5']/div[3]/a[1]").click()  # 确定
        sleep(1)
        self.driver.switch_to.frame(Frame4)
        self.driver.find_element_by_xpath("//tr[@id='FinanceTR']/td/input[2]").click()  # 财务科目:
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(Frame6)
        self.driver.find_element_by_xpath("//span[@id='mytree_2_ico']").click()  # 资产
        sleep(1)
        self.driver.find_element_by_xpath("//div[@class='pDiv']/div/a[4]").click()  # 最后一页
        sleep(1)
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr[3]/td[1]/div/input").click()  # 二级枚举科目
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer6']/div[3]/a[1]").click()  # 确定
        sleep(1)
        self.driver.switch_to.frame(Frame4)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@class='layui-layer-btn layui-layer-btn-']/a[1]").click()  # 保存
        sleep(1)
        self.driver.switch_to.default_content()
        Msg6 = self.driver.find_element_by_xpath("//div[@class='dialog_main_content_html ']").text  #
        print(Msg6)  # 保存成功
        self.driver.find_element_by_xpath("//span[@class='right padding_t_10 padding_r_10']/a[1]").click()  # 确定
        sleep(1)

    # def test_b_config(self):
    #     self.driver.get(self.base_url)
    #     self.driver.maximize_window()
    #     self.driver.find_element_by_css_selector("#login_username").send_keys("cxa")  #
    #     sleep(1)
    #     self.driver.find_element_by_css_selector("#login_password").send_keys("123456")  # 密码
    #     sleep(1)
    #     self.driver.find_element_by_css_selector("#login_button").click()
    #     self.driver.implicitly_wait(10)  # 等待，直到超出10s还未定位到元素则异常
    #     ZJM = self.driver.current_window_handle
    #     sleep(1)
    #     self.driver.find_element_by_xpath("//table[@title='普通科目配置带入表单']/tbody/tr/td[2]/a").click(  )  # 普通科目配置带入表单
    #     sleep(1)
    #     Win = self.driver.window_handles  # 所有窗口句柄
    #     for windows in Win:
    #         if windows != ZJM:
    #             self.driver.switch_to.window(windows)
    #             # print("系统配置界面窗口名称：",self.driver.title)
    #             sleep(1)

        # self.driver.switch_to.frame("zwIframe")
        self.driver.switch_to.window(ZJM)
        sleep(1)
        self.driver.find_element_by_xpath("//table[@title='普通科目配置带入表单']/tbody/tr/td[2]/a").click()  # 普通科目配置带入表单
        sleep(1)
        Win3 = self.driver.window_handles  # 所有窗口句柄
        for windows3 in Win3:
            if windows3 != ZJM:
                self.driver.switch_to.window(windows3)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(1)
        # self.driver.find_element_by_xpath("//input[@id='subject']").click()
        # sleep(1)
        self.driver.switch_to.frame("zwIframe")
        self.driver.find_element_by_xpath("//div[@class='render-eg__rightbox']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='account_field0001']").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("layui-layer-iframe1")
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr/td/div/input").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer1']/div[3]/a[1]").click(  )  # 保存
        sleep(1)
        self.driver.switch_to.frame("zwIframe")
        self.driver.find_element_by_xpath("//div[@class='cap4-depart__picker']").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("layui-layer-iframe2")
        sleep(1)
        self.driver.find_element_by_xpath("//div[@title='监查室']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//span[@class='select_selected']").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer2']/div[3]/a[1]").click()  # 保存
        sleep(1)
        self.driver.switch_to.frame("zwIframe")
        self.driver.find_element_by_xpath("//div[@id='field0004_id']/section/div[2]/div/div/div/input").click(  )  # 多级枚举
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='field0004_scnt']/div[2]/div").click(  )  # 一级枚举A
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='field0005_id']/section/div[2]/div/div/div/input").click(  )#
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='field0005_scnt']/div[2]/div").click()  # 二级枚举A
        sleep(1)
        self.driver.find_element_by_xpath("//div[@class='icon CAP cap-icon-xuanren']").click(  )  # 人员
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("layui-layer-iframe3")
        sleep(1)
        self.driver.find_element_by_xpath("//select[@id='memberDataBody']/option[4]").click(  )#
        sleep(1)
        self.driver.find_element_by_xpath("//span[@class='select_selected']").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//div[@id='layui-layer3']/div[3]/a[1]").click()  # 保存
        sleep(1)
        self.driver.switch_to.frame("zwIframe")
        self.driver.find_element_by_xpath("//div[@id='field0007_id']/section/div[2]/div/input").send_keys("收付转")
        sleep(1)
        self.driver.find_element_by_xpath("//input[@id='field0003_format']").send_keys("2019-12-25")
        sleep(1)
        self.driver.find_element_by_xpath \
            ("//section[@id='tableName-front_formson_1']/div[2]/div/section/div[2]/section/table/tbody/tr[2]/td[2]/div/section/div[2]/div/div/div/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@class='cap4-scontent']/div[2]/div").click(  )  # 差旅费
        sleep(1)
        self.driver.find_element_by_xpath \
            ("//section[@id='tableName-front_formson_1']/div[2]/div/section/div[2]/section/table/tbody/tr[2]/td[3]/div/section/div/div/div[2]/input").send_keys \
            ("10000")
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[@id='sendId']").click(  )  # 发送
        sleep(1)
        self.driver.switch_to.window(ZJM)
        self.driver.find_element_by_xpath("//div[@title='协同工作']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@title='待办事项']/div[2]").click()
        sleep(1)
        self.driver.switch_to.frame("mainIframe")
        self.driver.find_element_by_xpath("//div[@class='menu_item active_item']/div[2]").click(  )  # 全部待办
        sleep(1)
        ZJM_1 = self.driver.current_window_handle
        inputBox = self.driver.find_element_by_xpath("//tbody[@id='list']/tr[1]/td[2]/div/span")
        # 开始模拟鼠标双击操作
        ActionChains(self.driver).double_click(inputBox).perform()
        sleep(3)
        Win1 = self.driver.window_handles  # 所有窗口句柄
        for windows1 in Win1:
            if windows1 != ZJM_1:
                self.driver.switch_to.window(windows1)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(2)
        # self.driver.find_element_by_xpath("//input[@id='attitude_2']").click()
        self.driver.find_element_by_xpath("//textarea[@id='content_deal_comment']").send_keys("恭喜四川迈锐思科技有限公司完成①亿的小目标，必须手动点赞,100个赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞赞")
        sleep(3)
        self.driver.find_element_by_xpath("//div[@id='_dealDiv']/div[4]/input").click()
        sleep(1)
        self.driver.switch_to.frame("layui-layer-iframe1")
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='north']/button[4]").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//span[@class='right padding_t_10 padding_r_10']/a[1]").click()
        sleep(1)
        # self.driver.switch_to.frame("zwIframe")
        self.driver.switch_to.window(ZJM)
        self.driver.find_element_by_xpath("//div[@title='财务集成']").click()
        sleep(1)
        ZJM_2 = self.driver.current_window_handle
        sleep(1)
        move = self.driver.find_element_by_xpath("//div[@title='凭证制单']")  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        self.driver.find_element_by_xpath("//div[@title='凭证制单']").click()
        sleep(1)
        Win2 = self.driver.window_handles  # 所有窗口句柄
        for windows2 in Win2:
            if windows2 != ZJM_2:
                self.driver.switch_to.window(windows2)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(1)
        self.driver.switch_to.frame("myiframe")
        sleep(1)
        self.driver.find_element_by_xpath("//tbody[@id='list']/tr[1]/td[1]/div/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@id='east']/p/button[1]").click()
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("layui-layer-iframe1")
        sleep(1)
        self.driver.find_element_by_xpath("//button[@id='savepz']").click()
        sleep(3)















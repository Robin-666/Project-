from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from test_page.Public_method import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class LogZJ(BasePage):
    # driver = webdriver.Chrome()
    #初始化
    username_ID = (By.XPATH,"//input[@id='login_username']")#登录界面输入操作
    pwd = (By.XPATH,"//input[@id='login_password']")
    button = (By.XPATH,"//input[@id='login_button']")
    Select_CWJC = (By.XPATH,"//div[@title='财务集成']")
    Select_sys_config = (By.XPATH,"//div[@title='系统配置']")
    Select_Sub_config = (By.XPATH, "//div[@title='科目配置']")




    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_ID).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        #        self.find_element(*self.password_loc).clear()
        self.find_element(*self.pwd).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.button).click()

    def CWJC(self):#点击财务集成
        self.find_element(*self.Select_CWJC).click()
        global ZJM
        ZJM = self.driver.current_window_handle
    def Win_XF(self):#鼠标悬浮到系统配置
        move = self.find_element(*self.Select_sys_config)  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(1)
        self.driver.find_element(*self.Select_sys_config).click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from test_page.Public_method import BasePage


class Main(BasePage):

    username_ID = (By.XPATH,"//input[@id='login_username']")
    pwd = (By.XPATH,"//input[@id='login_password']")
    button = (By.XPATH,"//input[@id='login_button']")


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

    # 用户名或密码不合理是Tip框内容展示
    # def show_span(self):
    #     return self.find_element(*self.span_loc).text
    #
    # # 切换登录模式为动态密码登录（IE下有效）
    # def swich_DynPw(self):
    #     self.find_element(*self.dynpw_loc).click()
    #
    # # 登录成功页面中的用户ID查找
    # def show_userid(self):
    #     return self.find_element(*self.userid_loc).text





    
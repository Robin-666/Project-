from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from test_page.Public_method import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Subject_Config_JM(BasePage):#科目配置界面元素
    username_ID = (By.XPATH, "//input[@id='login_username']")  # 登录界面输入操作
    pwd = (By.XPATH, "//input[@id='login_password']")
    button = (By.XPATH, "//input[@id='login_button']")
    Select_CWJC = (By.XPATH, "//div[@title='财务集成']")
    Select_sys_config = (By.XPATH, "//div[@title='系统配置']")
    Select_Sub_config_xpath = (By.XPATH, "//div[@title='科目配置']")

    Select_XT_Work_xpath = (By.XPATH, "//div[@title='协同工作']")
    def Select_XT_Work(self):#协同工作
        self.find_element(*self.Select_XT_Work_xpath).click()

    #科目配置界面
    DF_KM_config = (By.XPATH,"//li[@id='tab2']")#贷方科目配置
    Year2019 = (By.XPATH,"//select[@id='acctYear2']")#2019
    YWMJ = (By.XPATH,"//select[@id='SubMapping2']")#业务枚举选择框


    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)
        sleep(1)
    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_ID).send_keys(username)
        sleep(1)
    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.pwd).send_keys(password)
        sleep(1)
    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.button).click()
        sleep(1)
    def CWJC(self):#点击财务集成
        # self.find_element(*self.Select_CWJC).click()
        move1 = self.find_element(*self.Select_CWJC)  # 鼠标悬停
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(move1).perform()
        self.driver.implicitly_wait(10)
        global ZJM
        ZJM = self.driver.current_window_handle
        sleep(1)

    Select_PZZD_config = (By.XPATH, "//div[@title='凭证制单']")
    def Win_PZZD(self):#鼠标悬浮到凭证制单
        move = self.find_element(*self.Select_PZZD_config)  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(1)
        self.driver.find_element(*self.Select_PZZD_config).click()
        sleep(1)

    # Select_CW_config = (By.XPATH, "//div[@title='财务集成']")
    def Win_XF(self):  # 鼠标悬浮到财务集成
        move = self.find_element(*self.Select_sys_config)  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(1)
        self.driver.find_element(*self.Select_sys_config).click()
        sleep(1)

    def Win_Split(self):#窗口切换
        global ZJM
        Win = self.driver.window_handles  # 所有窗口句柄
        for windows in Win:
            if windows != ZJM:
                self.driver.switch_to.window(windows)
                # print("系统配置界面窗口名称：",self.driver.title)
                sleep(2)


    People_Click_path = (By.XPATH,"//div[@title = '人员对照']")
    def People_Click(self):
        self.find_element(*self.People_Click_path).click()
        sleep(1)

    CXB_click_path = (By.XPATH,"//div[@title='崔雄B']")
    def CXB_click(self):
        self.find_element(*self.CXB_click_path).click()
        sleep(1)

    CXD_click_path = (By.XPATH, "//div[@title='崔雄D']")
    def CXD_click(self):
        self.find_element(*self.CXD_click_path).click()
        sleep(1)


    Right_ico_path = (By.XPATH,"//div[@id='east_center']/div/div[6]/div/a[3]")
    def Right_ico(self):
        self.find_element(*self.Right_ico_path).click()
        sleep(1)

    Save_Bind_path = (By.XPATH,"//a[@id='addbtn']")
    def Save_Bind(self):
        self.find_element(*self.Save_Bind_path).click()
        sleep(1)


    '''ERP配置界面'''
    Select_ERP_config = (By.XPATH, "//div[@title='ERP版本']")
    def ERP_config_Button(self):
        self.find_element(*self.Select_ERP_config).click()





    '''科目配置主界面'''
    def Sbu_Config(self):#科目配置
        self.find_element(*self.Select_Sub_config_xpath).click()

    def DF_Button(self):
        self.find_element(*self.DF_KM_config).click()
        sleep(1)
    def select_2019(self):
        sel = self.find_element(*self.Year2019)
        Select(sel).select_by_value("2019")
        sleep(1)

    Year2020 = (By.XPATH, "//select[@id='acctYear2']")  # 2020
    def select_2020(self):
        sel = self.find_element(*self.Year2020)
        Select(sel).select_by_value("2020")
        sleep(1)

    JF_Year2020 = (By.XPATH, "//select[@id='acctYear1']")  # 2020
    def JF_select_2020(self):
        sel = self.find_element(*self.JF_Year2020)
        Select(sel).select_by_value("2020")
        sleep(1)

    JF_YWMJ = (By.XPATH, "//select[@id='SubMapping1']")  # 业务枚举选择框
    def JF_select_YWDJMJ_A(self):#多级枚举-单位枚举(单位A)
        sel = self.find_element(*self.JF_YWMJ)
        Select(sel).select_by_visible_text("多级枚举-单位枚举(单位A)")
        sleep(1)

    JJF_ZT = (By.XPATH, "//select[@id='account1']")  # 所有账套
    def JF_ZT_and_001(self):
        sel = self.find_element(*self.JJF_ZT)
        Select(sel).select_by_visible_text("测试帐套001[001]")
        sleep(1)


    def select_YWMJDJ(self):#业务枚举多级-业务枚举(单位A)
        sel = self.find_element(*self.YWMJ)
        Select(sel).select_by_visible_text("业务枚举多级-业务枚举(单位A)")
        sleep(1)

    def select_YWDJMJ_A(self):#多级枚举-单位枚举(单位A)
        sel = self.find_element(*self.YWMJ)
        Select(sel).select_by_visible_text("多级枚举-单位枚举(单位A)")
        sleep(1)

    def select_QJ(self):#请假类型-公共枚举
        sel = self.find_element(*self.YWMJ)
        Select(sel).select_by_visible_text("请假类型-公共枚举")
        sleep(1)

    def select_Free_Text(self):#映射文本-自由文本(单位A)
        sel = self.find_element(*self.YWMJ)
        Select(sel).select_by_visible_text("映射文本-自由文本(单位A)")
        sleep(1)

    def select_N6N9(self):#映射文本-自由文本(单位A)
        sel = self.find_element(*self.YWMJ)
        Select(sel).select_by_visible_text("N6/N9支出事项-系统档案(单位A)")
        sleep(1)


    DF_ZT = (By.XPATH, "//select[@id='account2']")  # 所有账套
    New_Add = (By.XPATH, "//a[@id='ClkAdd2']")  # 新增
    def DF_ZT_and_All(self):
        sel = self.find_element(*self.DF_ZT)
        Select(sel).select_by_visible_text("全部")
        sleep(1)

    def DF_ZT_and_001(self):
        sel = self.find_element(*self.DF_ZT)
        Select(sel).select_by_visible_text("测试帐套001[001]")
        sleep(1)

    def DF_ZT_and_002(self):
        sel = self.find_element(*self.DF_ZT)
        Select(sel).select_by_visible_text("平行记帐测试账套002[002]")
        sleep(1)

    New_Add_JF = (By.XPATH, "//a[@id='ClkAdd1']")  # 新增
    def Add_Button_JF(self):
        self.find_element(*self.New_Add_JF).click()
        sleep(1)


    def Add_Button(self):
        self.find_element(*self.New_Add).click()
        sleep(1)
    ZT_info = (By.XPATH, "//tr[@id='ConfigTR1']/td/input[5]")
    def addInZT(self):
        self.find_element(*self.ZT_info).click()
        sleep(1)
    del_path = (By.XPATH,"//a[@id='ClkDel2']")
    def Dele(self):
        self.find_element(*self.del_path).click()
        sleep(1)

    OK_Msg_path = (By.XPATH,"//span[@class='right padding_t_10 padding_r_10']/a[1]")
    def OK_Msg(self):
        self.find_element(*self.OK_Msg_path).click()
        sleep(1)

    NG_Msg_path = (By.XPATH, "//span[@class='right padding_t_10 padding_r_10']/a[2]")
    def NG_Msg(self):
        self.find_element(*self.NG_Msg_path).click()
        sleep(1)

    ALL_List_path1 = (By.XPATH,"//div[@id='tab2_div']/div[2]/div[3]/div/table/thead/tr/th[1]/div/input")
    def ALL_List(self):#全选
        self.find_element(*self.ALL_List_path1).click()
        sleep(1)

    TC_info = (By.XPATH, "//div[@class='dialog_main_content_html ']")
    def Dialog(self):
        Msg = self.find_element(*self.TC_info).text
        sleep(1)
        print(Msg)
        return Msg

    ZJM_first_one_path = (By.XPATH, "//tbody[@id='list']/tr[1]/td[7]")
    def ZJM_first_one_text(self):
        Lab = self.find_element(*self.ZJM_first_one_path).text
        print(Lab)
        return Lab

    ZJM_first_two_path = (By.XPATH, "//tbody[@id='list']/tr[2]/td[7]")
    def ZJM_first_two_text(self):
        Lab = self.find_element(*self.ZJM_first_two_path).text
        print(Lab)
        return Lab

    ZJM_first_three7_path = (By.XPATH, "//tbody[@id='list']/tr[3]/td[7]")
    def ZJM_first_three7_text(self):
        Lab = self.find_element(*self.ZJM_first_three7_path).text
        print(Lab)
        return Lab

    ZJM_first_four7_path = (By.XPATH, "//tbody[@id='list']/tr[4]/td[7]")
    def ZJM_first_four7_text(self):
        Lab = self.find_element(*self.ZJM_first_four7_path).text
        print(Lab)
        return Lab

    ZJM_first_one_path1 = (By.XPATH, "//tbody[@id='list']/tr[1]/td[12]")
    def ZJM_first_one_text_12(self):
        Lab = self.find_element(*self.ZJM_first_one_path1).text
        print(Lab)
        return Lab

    ZJM_first_two_path1 = (By.XPATH, "//tbody[@id='list']/tr[2]/td[12]")
    def ZJM_first_two_text_12(self):
        Lab = self.find_element(*self.ZJM_first_two_path1).text
        print(Lab)
        return Lab


    ZJM_first_three_path = (By.XPATH, "//tbody[@id='list']/tr[3]/td[12]")
    def ZJM_first_three_text(self):
        Lab = self.find_element(*self.ZJM_first_three_path).text
        print(Lab)
        return Lab

    ZJM_first_four_path = (By.XPATH, "//tbody[@id='list']/tr[4]/td[12]")
    def ZJM_first_four_text(self):
        Lab = self.find_element(*self.ZJM_first_four_path).text
        print(Lab)
        return Lab

    ZJM_List_three_path = (By.XPATH,"//tbody[@id='list']/tr[3]/td[1]/div/input")
    def ZJM_List_three(self):
        self.find_element(*self.ZJM_List_three_path).click()
        sleep(1)

    ZJM_List_four_path = (By.XPATH, "//tbody[@id='list']/tr[4]/td[1]/div/input")
    def ZJM_List_four(self):
        self.find_element(*self.ZJM_List_four_path).click()
        sleep(1)

    XG_BUTTON_path = (By.XPATH,"//a[@id='ClkEdit2']")
    def ZJM_XG_Button(self):#修改按钮
        self.find_element(*self.XG_BUTTON_path).click()
        sleep(1)

    ZJM_All_list_path = (By.XPATH, "//div[@id='tab2_div']/div[2]/div[5]")
    def ZJM_All_list(self):
        Lab = self.find_element(*self.ZJM_All_list_path).text
        sleep(1)
        print("Lab此处应该为：空", Lab)
        return Lab

    Search_Button_path = (By.XPATH,"//div[@id='searchInfo2']")
    def ZJM_Search_Button(self):
        self.find_element(*self.Search_Button_path).click()
        sleep(1)

    Search_Button_DXMC_path = (By.XPATH, "//div[@id='tab2_div']/div[3]/div/div[2]/p[2]")
    def ZJM_Search_Button_DXMC(self):  # 对象名称
        self.find_element(*self.Search_Button_DXMC_path).click()
        sleep(1)

    Search_Button_CW_path = (By.XPATH, "//div[@id='tab2_div']/div[3]/div/div[2]/p[3]")
    def ZJM_Search_Button_CW(self):  # 财务科目
        self.find_element(*self.Search_Button_CW_path).click()
        sleep(1)

    Search_Button_SJ_path = (By.XPATH, "//div[@id='tab2_div']/div[3]/div/div[2]/p[4]")
    def ZJM_Search_Button_SJ(self):  # 税金科目
        self.find_element(*self.Search_Button_SJ_path).click()
        sleep(1)

    Search_Button_BM_path = (By.XPATH, "//div[@id='tab2_div']/div[3]/div/div[2]/p[6]")
    def ZJM_Search_Button_BM(self):  # 部门名称
        self.find_element(*self.Search_Button_BM_path).click()
        sleep(1)

    Search_Button_Input_path =(By.XPATH,"//input[@id='searchInput2']")
    def ZJM_Search_Button_Input(self,key):
        self.find_element(*self.Search_Button_Input_path).send_keys(key)
        sleep(1)

    # Search_Button_SJ_Input_path = (By.XPATH, "//input[@id='searchInput1']")
    # def ZJM_Search_Button_SJ_Input(self, key):#税金输入
    #     self.find_element(*self.Search_Button_SJ_Input_path).send_keys(key)
    #     sleep(1)

    Search_Button_TB_path = (By.XPATH, "//p[@id='clkSearch2']/i")
    def ZJM_Search_Button_TB(self):
        self.find_element(*self.Search_Button_TB_path).click()
        sleep(1)

    def ZJM_Clear_Button_Input(self):
        self.find_element(*self.Search_Button_Input_path).clear()
        sleep(1)

    NJ_path = (By.XPATH,"//a[@id='YearEnd2']")
    def NJ_Button(self):
        self.find_element(*self.NJ_path).click()
        sleep(1)
    '''贷方科目配置'''
    SJ_config_path = (By.XPATH, "//li[@id='tab3']")  # 贷方科目配置
    def SJ_Button(self):
        self.find_element(*self.SJ_config_path).click()
        sleep(1)

    SJ_ZT_ALL_path = (By.XPATH,"//select[@id='account3']")
    def SJ_ZT_All(self):
        sel = self.find_element(*self.SJ_ZT_ALL_path)
        Select(sel).select_by_visible_text("全部")
        sleep(1)

    SJ_ZT_001_path = (By.XPATH, "//select[@id='account3']")
    def SJ_ZT_001(self):
        sel = self.find_element(*self.SJ_ZT_001_path)
        Select(sel).select_by_visible_text("测试帐套001[001]")
        sleep(1)

    def SJ_ZT_002(self):
        sel = self.find_element(*self.SJ_ZT_001_path)
        Select(sel).select_by_visible_text("平行记帐测试账套002[002]")
        sleep(1)

    SJ_Add_Button_path = (By.XPATH,"//a[@id='ClkAdd3']")
    def SJ_Add_Button(self):
        self.find_element(*self.SJ_Add_Button_path).click()
        sleep(1)

    Change_Year_path = (By.XPATH, "//a[@id='ClkEdit3']")
    def Change_Year_button(self):
        self.find_element(*self.Change_Year_path).click()






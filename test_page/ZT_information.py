from selenium.webdriver.common.by import By
from test_page.Public_method import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class ZT_ZM(BasePage):
    '''查询条件   账套信息界面'''
    CX_TJ_name =(By.XPATH,"//a[@title='按账套名称查询']")
    name_input =(By.XPATH,"//li[@id='acctnm_container']/input")
    CX_TJ = (By.XPATH,"//table[@class='ellipsis_table']")#查询条件
    def ZT_name(self):
        self.find_element(*self.CX_TJ).click()
        sleep(1)
        self.find_element(*self.CX_TJ_name).click()
        sleep(1)

    def ZT_name_clear(self):#清除查询条件
        self.find_element(*self.name_input).clear()
        sleep(1)
    #按账套号
    name_input1 = (By.XPATH, "//li[@id='acctid_container']/input")
    def Send_KEY(self, Value):
        self.find_element(*self.name_input1).send_keys(Value)
        sleep(1)

    # 按账套名称
    def Send_KEY_name(self, Value):
        self.find_element(*self.name_input).send_keys(Value)
        sleep(1)

    CX_TJ_Num = (By.XPATH, "//a[@title='按账套号查询']")
    def ZT_Num(self):
        self.find_element(*self.CX_TJ).click()
        sleep(1)
        self.find_element(*self.CX_TJ_Num).click()
        sleep(1)

    def ZT_Num_clear(self):
        self.find_element(*self.name_input1).clear()
        sleep(1)


    CX_TJ_year = (By.XPATH, "//a[@title='按年度查询']")
    def ZT_year(self):
        self.find_element(*self.CX_TJ).click()
        sleep(1)
        self.find_element(*self.CX_TJ_year).click()
        sleep(1)

    year_input =(By.XPATH,"//li[@id='year_container']/input")
    def ZT_year_clear(self):
        self.find_element(*self.year_input).clear()
        sleep(1)

    def Send_KEY_year(self, Value):
        self.find_element(*self.year_input).send_keys(Value)
        sleep(1)



    CX_Button = (By.XPATH,"//li[@class='margin_l_5 search_btn']/a")
    def Check_Button(self):
        self.find_element(*self.CX_Button).click()
        sleep(1)

    Lab1_path1 = (By.XPATH,"//tbody[@id='list']/tr[1]/td[2]")#年度
    Lab1_path2 = (By.XPATH, "//tbody[@id='list']/tr[1]/td[4]")#账套名称
    def Lab1(self):
        # lab1 = self.find_element(*self.Lab1_path1).text
        lab2 = self.find_element(*self.Lab1_path2).text
        print(lab2)
        return lab2

    def Lab1_1(self):
        lab1 = self.find_element(*self.Lab1_path1).text
        # lab2 = self.find_element(*self.Lab1_path2).text
        print(lab1)
        return lab1

    Lab2_path1 = (By.XPATH, "//tbody[@id='list']/tr[2]/td[2]")
    Lab2_path2 = (By.XPATH, "//tbody[@id='list']/tr[2]/td[4]")
    def Lab2(self):
        # lab1 = self.find_element(*self.Lab1_path1).text
        lab2 = self.find_element(*self.Lab2_path2).text
        print(lab2)
        return lab2

    Lab3_path1 = (By.XPATH, "//tbody[@id='list']/tr[3]/td[2]")
    Lab3_path2 = (By.XPATH, "//tbody[@id='list']/tr[3]/td[4]")
    def Lab3(self):
        # lab1 = self.find_element(*self.Lab3_path1).text
        lab2 = self.find_element(*self.Lab3_path2).text
        print(lab2)
        return lab2
    LAB_ALL = (By.XPATH, "//table[@id='MyTable']")
    def Lab4(self):
        lab2 = self.find_element(*self.LAB_ALL).text
        print("此处应为空：",lab2)
        return lab2
    F1 = (By.XPATH,"//table[@id='MyTable']/tbody/tr[1]/td[1]/div/input")
    def First_one(self):
        # inputBox = self.find_element(*self.F1)
        # # 开始模拟鼠标双击操作
        # ActionChains(self.driver).double_click(inputBox).perform()
        # sleep(1)
        self.find_element(*self.F1).click()
        sleep(1)

    get_Value = (By.XPATH,"//tr[@id='ConfigTR1']/td/input[5]")
    def ZT_infor_input(self):#获取账套输入框的值
        Data = self.find_element(*self.get_Value).get_attribute("value")
        print(Data)
        return Data

    get_Value_YWMJ = (By.XPATH, "//tr[@id='ConfigTR2']/td/input[2]")
    def ZT_infor_input_YWMJ(self):#获取业务枚举多级输入框的值
        Data = self.find_element(*self.get_Value_YWMJ).get_attribute("value")
        print(Data)
        return Data

    get_Value_CWKM = (By.XPATH,"//tr[@id='FinanceTR']/td/input[2]")
    def ZT_infor_input_CWKM(self):
        Data = self.find_element(*self.get_Value_CWKM).get_attribute("value")
        print(Data)
        return Data

    get_Value_CWSJ = (By.XPATH, "//tr[@id='TaxTR']/td/input[2]")
    def ZT_infor_input_CWSJ(self):
        Data = self.find_element(*self.get_Value_CWSJ).get_attribute("value")
        print(Data)
        return Data



    F3 = (By.XPATH, "//table[@id='MyTable']/tbody/tr[3]/td[1]/div/input")
    def First_three(self):
        self.find_element(*self.F3).click()
        sleep(1)

    save_frame1_path = (By.XPATH, "//div[@id='layui-layer1']/div[3]/a[1]")
    def Save_frame1(self):
        self.find_element(*self.save_frame1_path).click()
        sleep(1)

    save_frame2_path = (By.XPATH,"//div[@id='layui-layer2']/div[3]/a[1]")#确定
    def Save_frame2(self):
        self.find_element(*self.save_frame2_path).click()
        sleep(1)

    save_frame3_path = (By.XPATH, "//div[@id='layui-layer3']/div[3]/a[1]")  # 确定
    def Save_frame3(self):
        self.find_element(*self.save_frame3_path).click()
        sleep(1)

    save_frame4_path = (By.XPATH, "//div[@id='layui-layer4']/div[3]/a[1]")  # 确定
    def Save_frame4(self):
        self.find_element(*self.save_frame4_path).click()
        sleep(1)

    clear_frame3 = (By.XPATH, "//div[@id='layui-layer3']/div[3]/a[2]")#清空
    def Clear_frame2(self):
        self.find_element(*self.clear_frame3).click()
        sleep(1)

    clear_frame222 = (By.XPATH, "//div[@id='layui-layer2']/div[3]/a[2]")  # 清空
    def Clear_22frame2(self):
        self.find_element(*self.clear_frame222).click()
        sleep(1)

    KM_Row1 = (By.XPATH, "//tr[@id='ConfigTR1']/td/input[5]")
    def Click_Row1(self):
        self.find_element(*self.KM_Row1).click()
        sleep(1)

    KM_Row2 = (By.XPATH,"//tr[@id='ConfigTR2']/td/input[2]")
    def Click_Row2(self):
        self.find_element(*self.KM_Row2).click()
        sleep(1)
    TC_info = (By.XPATH,"//div[@class='dialog_main_content_html ']")
    def Dialog(self):
        Msg = self.find_element(*self.TC_info).text
        sleep(1)
        print(Msg)
        return Msg
    KM_Row4 = (By.XPATH, "//tr[@id='FinanceTR']/td/input[2]")
    def Click_Row4(self):
        self.find_element(*self.KM_Row4).click()
        sleep(1)

    KM_Row5 = (By.XPATH, "//tr[@id='TaxTR']/td/input[2]")
    def Click_Row5(self):
        self.find_element(*self.KM_Row5).click()
        sleep(1)

    KM_Row6 = (By.XPATH, "//tr[@id='BudgetTR']/td/input[2]")
    def Click_Row6(self):
        self.find_element(*self.KM_Row6).click()
        sleep(1)

    KM_Row3 = (By.XPATH, "//tr[@id='DeptTR']/td/input[2]")
    def Click_Row3(self):
        self.find_element(*self.KM_Row3).click()
        sleep(1)

    '''映射信息界面'''
    Input_text_path = (By.XPATH,"//li[@class='common_search_input']/input")
    def Input_text(self):
        self.find_element(*self.Input_text_path).click()
        sleep(1)

    def Input_send_key(self,KEY):
        self.find_element(*self.Input_text_path).send_keys(KEY)
        sleep(1)

    search_Bu_path = (By.XPATH,"//a[@id='search_btn']/em")
    def search_Button(self):
        self.find_element(*self.search_Bu_path).click()
        sleep(1)

    span3_text_path =(By.XPATH,"//span[@id='mytree_3_span']")
    def span_text_AA(self):
        Lab = self.find_element(*self.span3_text_path).text
        print(Lab)
        sleep(1)
        return Lab

    span6_text_path = (By.XPATH, "//span[@id='mytree_6_span']")
    def span_text_AB(self):
        Lab = self.find_element(*self.span6_text_path).text
        print(Lab)
        sleep(1)
        return Lab

    def Click_mytree_6_span(self):
        self.find_element(*self.span6_text_path).click()
        sleep(1)


    span7_text_path = (By.XPATH, "//span[@id='mytree_7_span']")
    def span_text_B(self):
        self.find_element(*self.span7_text_path).click()

    span2_text_path = (By.XPATH,"//span[@id='mytree_2_span']")
    def span_text_A(self):
        self.find_element(*self.span2_text_path).click()

    mytree_2 = (By.XPATH,"//span[@id='mytree_2_switch']")
    def mytree_2_switch(self):#展开业务枚举一级A
        self.find_element(*self.mytree_2).click()
        sleep(1)

    def mytree_3_span(self):
        self.find_element(*self.span3_text_path).click()
        sleep(1)

    list_01 = (By.XPATH,"//tbody[@id='list']/tr[1]/td[3]")
    def Tbody_list_01(self):
        LAB = self.find_element(*self.list_01).text
        print(LAB)
        sleep(1)
        return LAB

    list_02 = (By.XPATH, "//tbody[@id='list']/tr[2]/td[3]")
    def Tbody_list_02(self):
        LAB = self.find_element(*self.list_02).text
        print(LAB)
        sleep(1)
        return LAB

    list_03 = (By.XPATH, "//tbody[@id='list']/tr[3]/td[3]")
    def Tbody_list_03(self):
        LAB = self.find_element(*self.list_03).text
        print(LAB)
        sleep(1)
        return LAB

    list_01_01 = (By.XPATH, "//tbody[@id='list']/tr[1]/td[1]/div/input")
    def First_td_01(self):
        self.find_element(*self.list_01_01).click()
        sleep(1)


    YS_search_path = (By.XPATH,"//table[@class='ellipsis_table']/tbody/tr/td[1]")
    def YS_search_button(self):
        self.find_element(*self.YS_search_path).click()
        sleep(1)

    YS_search_name_path = (By.XPATH,"//a[@title='名称']")
    def YS_search_name(self):
        self.find_element(*self.YS_search_name_path).click()
        sleep(1)

    YS_send_input_name_path = (By.XPATH,"//li[@id='name_container']/input")
    def YS_send_key(self,key):
        self.find_element(*self.YS_send_input_name_path).send_keys(key)
        sleep(1)

    def clear_YS_send_key(self):
        self.find_element(*self.YS_send_input_name_path).clear()
        sleep(1)

    YS_check_path = (By.XPATH,"//a[@class='common_button  search_buttonHand']")
    def YS_Check_button(self):
        self.find_element(*self.YS_check_path).click()
        sleep(1)

    YS_All_list_path = (By.XPATH,"//table[@id='mytable']")
    def YS_All_list(self):
        Lab = self.find_element(*self.YS_All_list_path).text
        sleep(1)
        print("Lab此处应该为：空",Lab)
        return Lab



    '''财务科目界面'''

    CW_Input_path =(By.XPATH,"//div[@id='north']/div/ul/li/input")
    def CW_INPUT_Key(self,key):
        self.find_element(*self.CW_Input_path).send_keys(key)
        sleep(1)

    CW_search_button = (By.XPATH,"//a[@id='search_btn']")
    def CW_search(self):
        self.find_element(*self.CW_search_button).click()
        sleep(1)

    CW_mytree_1_span_path = (By.XPATH,"//span[@id='mytree_1_span']")
    def CW_mytree_1_span(self):#科目
        self.find_element(*self.CW_mytree_1_span_path).click()
        sleep(1)

    CW_mytree_2_span_path = (By.XPATH,"//span[@id='mytree_2_span']")
    def CW_mytree_2_span(self):#资产
        self.find_element(*self.CW_mytree_2_span_path).click()
        sleep(1)

    CW_mytree_2_switch_path = (By.XPATH,"//span[@id='mytree_2_switch']")#资产中的展开按钮
    def CW_mytree_2_switch(self):
        self.find_element(*self.CW_mytree_2_switch_path).click()
        sleep(1)

    CW_mytree_4_span_path =(By.XPATH,"//span[@id='mytree_4_span']")
    def CW_mytree_4_span(self):
        self.find_element(*self.CW_mytree_4_span_path).click()
        sleep(1)

    CW_mytree_15_span_path = (By.XPATH,"//span[@id='mytree_15_span']")
    def CW_mytree_15_span(self):
        self.find_element(*self.CW_mytree_15_span_path).click()
        sleep(1)

    CW_mytree_22_span_path = (By.XPATH, "//span[@id='mytree_22_span']")
    def CW_mytree_22_span(self):
        self.find_element(*self.CW_mytree_22_span_path).click()
        sleep(1)


    CW_mytree_93_span_path = (By.XPATH,"//span[@id='mytree_93_span']")
    def CW_mytree_93_span(self):#负债
        self.find_element(*self.CW_mytree_93_span_path).click()
        sleep(1)

    CW_mytree_138_span_path = (By.XPATH,"//span[@id='mytree_138_span']")
    def CW_mytree_138_span(self):#共同
        self.find_element(*self.CW_mytree_138_span_path).click()
        sleep(1)

    CW_mytree_146_span_path = (By.XPATH,"//span[@id='mytree_146_span']")
    def CW_mytree_146_span(self):#权益
        self.find_element(*self.CW_mytree_146_span_path).click()
        sleep(1)

    CW_mytree_162_span_path = (By.XPATH,"//span[@id='mytree_162_span']")
    def CW_mytree_162_span(self):#损益
        self.find_element(*self.CW_mytree_162_span_path).click()
        sleep(1)

    CW_ZJXS = (By.XPATH,"//div[@class='pDiv']/div/span/span[1]")#共。。记录
    def CW_XSYS(self):
        Lab = self.find_element(*self.CW_ZJXS).text
        print(Lab)
        return Lab

    CW_YS_path = (By.XPATH, "//div[@class='pDiv']/div/span/span[2]")#总页数
    def CW_YS(self):
        Lab = self.find_element(*self.CW_YS_path).text
        print(Lab)
        return Lab

    CW_Last_page_path = (By.XPATH,"//span[@class='pageLast']")
    def CW_Last_page(self):
        self.find_element(*self.CW_Last_page_path).click()
        sleep(1)


    CW_mytree_20_span_path = (By.XPATH,"//span[@id='mytree_20_span']")
    def CW_mytree_20_span(self):
        Lab = self.find_element(*self.CW_mytree_20_span_path).text
        print(Lab)
        return Lab

    CW_mytree_107_span_path = (By.XPATH,"//span[@id='mytree_107_span']")
    def CW_mytree_107_span(self):
        Lab = self.find_element(*self.CW_mytree_107_span_path).text
        print(Lab)
        return Lab
    CW_first_one_path = (By.XPATH,"//tbody[@id='list']/tr[1]/td[1]/div/input")
    CW_first_two_path = (By.XPATH, "//tbody[@id='list']/tr[2]/td[1]/div/input")
    CW_first_three_path = (By.XPATH, "//tbody[@id='list']/tr[3]/td[1]/div/input")
    CW_first_four_path = (By.XPATH, "//tbody[@id='list']/tr[4]/td[1]/div/input")
    CW_first_five_path = (By.XPATH, "//tbody[@id='list']/tr[5]/td[1]/div/input")
    CW_first_six_path = (By.XPATH, "//tbody[@id='list']/tr[6]/td[1]/div/input")
    CW_first_seven_path = (By.XPATH, "//tbody[@id='list']/tr[7]/td[1]/div/input")
    CW_first_eight_path = (By.XPATH, "//tbody[@id='list']/tr[8]/td[1]/div/input")
    CW_first_nine_path = (By.XPATH, "//tbody[@id='list']/tr[9]/td[1]/div/input")
    CW_first_ten_path = (By.XPATH, "//tbody[@id='list']/tr[10]/td[1]/div/input")
    def CW_List_one(self):
        self.find_element(*self.CW_first_one_path).click()
        sleep(1)
    def CW_List_two(self):
        self.find_element(*self.CW_first_two_path).click()
        sleep(1)
    def CW_List_three(self):
        self.find_element(*self.CW_first_three_path).click()
        sleep(1)
    def CW_List_four(self):
        self.find_element(*self.CW_first_four_path).click()
        sleep(1)
    def CW_List_five(self):
        self.find_element(*self.CW_first_five_path).click()
        sleep(1)
    def CW_List_six(self):
        self.find_element(*self.CW_first_six_path).click()
        sleep(1)
    def CW_List_seven(self):
        self.find_element(*self.CW_first_seven_path).click()
        sleep(1)
    def CW_List_eigth(self):
        self.find_element(*self.CW_first_eight_path).click()
        sleep(1)
    def CW_List_nine(self):
        self.find_element(*self.CW_first_nine_path).click()
        sleep(1)
    def CW_List_ten(self):
        self.find_element(*self.CW_first_ten_path).click()
        sleep(1)

    CW_first_one_path1 = (By.XPATH, "//tbody[@id='list']/tr[1]/td[3]")
    CW_first_two_path1 = (By.XPATH, "//tbody[@id='list']/tr[2]/td[3]")
    CW_first_three_path1 = (By.XPATH, "//tbody[@id='list']/tr[3]/td[3]")
    CW_first_four_path1 = (By.XPATH, "//tbody[@id='list']/tr[4]/td[3]")
    CW_first_five_path1 = (By.XPATH, "//tbody[@id='list']/tr[5]/td[3]")
    CW_first_six_path1 = (By.XPATH, "//tbody[@id='list']/tr[6]/td[3]")
    CW_first_All = (By.XPATH, "//table[@id='mytable']")
    def CW_All_text(self):
        Lab = self.find_element(*self.CW_first_All).text
        print("Lab:",Lab)
        return Lab

    def CW_List_one1(self):
        Lab = self.find_element(*self.CW_first_one_path1).text
        print(Lab)
        return Lab
    def CW_List_two1(self):
        Lab = self.find_element(*self.CW_first_two_path1).text
        print(Lab)
        return Lab
    def CW_List_three1(self):
        Lab = self.find_element(*self.CW_first_three_path1).text
        print(Lab)
        return Lab
    def CW_List_four1(self):
        Lab = self.find_element(*self.CW_first_four_path1).text
        print(Lab)
        return Lab
    def CW_List_five1(self):
        Lab = self.find_element(*self.CW_first_five_path1).text
        print(Lab)
        return Lab
    def CW_List_six1(self):
        Lab = self.find_element(*self.CW_first_six_path1).text
        print(Lab)
        return Lab

    CW_TABLE = (By.XPATH,"//table[@class='ellipsis_table']/tbody/tr/td")
    CW_KMBM = (By.XPATH,"//a[@title='科目编码']")
    def Check_Input_KMBM(self):
        self.find_element(*self.CW_TABLE).click()
        sleep(1)
        self.find_element(*self.CW_KMBM).click()
        sleep(1)

    CW_ccode_container = (By.XPATH,"//li[@id='ccode_container']/input")#科目编码输入框
    def KMBM_Input(self,key):
        self.find_element(*self.CW_ccode_container).send_keys(key)
        sleep(1)

    def clear_KMBM_Input(self):
        self.find_element(*self.CW_ccode_container).clear()
        sleep(1)

    CW_KMMC = (By.XPATH,"//a[@title='科目名称']")
    def Check_Input_KMMC(self):
        self.find_element(*self.CW_TABLE).click()
        sleep(1)
        self.find_element(*self.CW_KMMC).click()
        sleep(1)

    CW_ccode_name_container_path = (By.XPATH,"//li[@id='ccode_name_container']/input")#科目名称输入框
    def KMMC_Input(self,key):
        self.find_element(*self.CW_ccode_name_container_path).send_keys(key)
        sleep(1)

    def Clear_KMMC_Input(self):
        self.find_element(*self.CW_ccode_name_container_path).clear()
        sleep(1)

    CW_JZC_path = (By.XPATH,"//span[@id='mytree_63_span']")#净资产
    def CW_JZC(self):
        self.find_element(*self.CW_JZC_path).click()
        sleep(1)


    '''部门科目界面'''

    ZK_Button_path = (By.XPATH,"//span[@id='myTree_29_switch']")
    def ZK_Button(self):#展开
        self.find_element(*self.ZK_Button_path).click()
        sleep(1)

    ZHKM_ZH = (By.XPATH,"//span[@id='myTree_32_check']")
    def Dep_ZH(self):
        self.find_element(*self.ZHKM_ZH).click()#综合科
        sleep(1)

    ZHKM_JCS = (By.XPATH, "//span[@id='myTree_33_check']")
    def Dep_JCS(self):
        self.find_element(*self.ZHKM_JCS).click()  # 监察室
        sleep(1)

    ZHKM_BGS = (By.XPATH, "//span[@id='myTree_30_check']")
    def Dep_BGS(self):
        self.find_element(*self.ZHKM_BGS).click()  # 办公室
        sleep(1)

    ZHKM_JBGS = (By.XPATH, "//span[@id='myTree_34_check']")
    def Dep_JBGS(self):
        self.find_element(*self.ZHKM_JBGS).click()  # 局办公室
        sleep(1)

    ZHKM_SZSZY = (By.XPATH, "//span[@id='myTree_35_check']")
    def Dep_SZSZY(self):
        self.find_element(*self.ZHKM_SZSZY).click()  # 水政水资源科
        sleep(1)

    ZHKM_ZKGWY_path = (By.XPATH,"//span[@id='myTree_37_switch']")
    def Dep_ZKGWY(self):
        self.find_element(*self.ZHKM_ZKGWY_path).click()  # 展开国务院
        sleep(1)

    ZHKM_CZB_path = (By.XPATH, "//span[@id='myTree_38_switch']")
    def Dep_CZB(self):
        self.find_element(*self.ZHKM_CZB_path).click()  # 展开财政部
        sleep(1)

    ZHKM_BGT = (By.XPATH, "//span[@id='myTree_39_check']")
    def Dep_BGT(self):
        self.find_element(*self.ZHKM_BGT).click()  # 办公厅
        sleep(1)

    ZHKM_ZHS = (By.XPATH, "//span[@id='myTree_40_check']")
    def Dep_ZHS(self):
        self.find_element(*self.ZHKM_ZHS).click()  # 综合司
        sleep(1)

    ZHKM_TFS = (By.XPATH, "//span[@id='myTree_41_check']")
    def Dep_TFS(self):
        self.find_element(*self.ZHKM_TFS).click()  # 条法司
        sleep(1)


    '''请假类型-公共枚举'''
    QJ_first_one_path = (By.XPATH, "//tbody[@id='list']/tr[1]/td[5]")
    def ZJM_QJ_one_text(self):
        Lab = self.find_element(*self.QJ_first_one_path).text
        print(Lab)
        return Lab

    QJ_first_two_path = (By.XPATH, "//tbody[@id='list']/tr[2]/td[5]")
    def ZJM_QJ_two_text(self):
        Lab = self.find_element(*self.QJ_first_two_path).text
        print(Lab)
        return Lab

    QJ_first_three_path = (By.XPATH, "//tbody[@id='list']/tr[3]/td[5]")
    def ZJM_QJ_three_text(self):
        Lab = self.find_element(*self.QJ_first_three_path).text
        print(Lab)
        return Lab

    QJ_first_four_path = (By.XPATH, "//tbody[@id='list']/tr[4]/td[5]")
    def ZJM_QJ_four_text(self):
        Lab = self.find_element(*self.QJ_first_four_path).text
        print(Lab)
        return Lab

    '''自由文本枚举'''
    Free_Row2 = (By.XPATH, "//tr[@id='ConfigTR2']/td/input[2]")
    def Free_Input_Row2(self,key):
        self.find_element(*self.Free_Row2).send_keys(key)
        sleep(1)

    '''N6N9枚举'''

    N6_ZCSX_A_path = (By.XPATH,"//span[@id='mytree_3_span']")
    def N6_A(self):
        self.find_element(*self.N6_ZCSX_A_path).click()
        sleep(1)

    N6_ZCSX_B_path = (By.XPATH, "//span[@id='mytree_4_span']")
    def N6_B(self):
        self.find_element(*self.N6_ZCSX_B_path).click()
        sleep(1)

    N6_ZCSX_C_path = (By.XPATH, "//span[@id='mytree_5_span']")
    def N6_C(self):
        self.find_element(*self.N6_ZCSX_C_path).click()
        sleep(1)

    '''税金科目配置界面'''
    SJ_row_01_path = (By.XPATH,"//tr[@id='ConfigTR1']/td/input[5]")
    def SJ_Click_Row1(self):
        self.find_element(*self.SJ_row_01_path).click()
        sleep(1)


    #进项税科目
    JXS_Deve_path = (By.XPATH,"//input[@id='inputnm']")
    def JXS_Deve_button(self):
        self.find_element(*self.JXS_Deve_path).click()
        sleep(1)

    # 销项税科目名称
    XXS_Deve_path = (By.XPATH,"//input[@id='outputnm']")
    def XXS_Deve_Input(self):
        self.find_element(*self.XXS_Deve_path).click()
        sleep(1)

    Year_2019_SJ_path = (By.XPATH,"//select[@id='acctYear3']")
    def Year_2019_SJ(self):
        sel = self.find_element(*self.Year_2019_SJ_path)
        Select(sel).select_by_value("2019")
        sleep(1)

    def Year_2020_SJ(self):
        sel = self.find_element(*self.Year_2019_SJ_path)
        Select(sel).select_by_value("2020")
        sleep(1)

    JXSE_SJ_path = (By.XPATH,"//div[@title = '进项税额']")
    def JXSE_SJ(self):
        self.find_element(*self.JXSE_SJ_path).click()

    XXSE_SJ_path = (By.XPATH, "//div[@title = '销项税额']")
    def XXSE_SJ(self):
        self.find_element(*self.XXSE_SJ_path).click()


    ZJM_Data_1_path = (By.XPATH,"//table[@id='myTable3']/tbody/tr[1]/td[6]")
    def ZJM_Data_Display_1(self):
        Lab1 = self.find_element(*self.ZJM_Data_1_path).text
        print(Lab1)
        return Lab1

    ZJM_Data_2_path = (By.XPATH, "//table[@id='myTable3']/tbody/tr[1]/td[8]")
    def ZJM_Data_Display_2(self):
        Lab1 = self.find_element(*self.ZJM_Data_2_path).text
        print(Lab1)
        return Lab1

    JZC_path = (By.XPATH,"//div[@title='行政事业盈余']")
    def JZC_Dispaly(self):
        self.find_element(*self.JZC_path).click()


    Lab_td_6_path = (By.XPATH,"//div[@title='22210101[应交税费-应交增值税-进项税额]']")
    def Lab_td_6(self):
        self.find_element(*self.Lab_td_6_path).click()

    Lab_td_8_path = (By.XPATH,"//div[@title='320101[本年盈余-行政事业盈余]']")
    def Lab_td_8(self):
        self.find_element(*self.Lab_td_8_path).click()


    Year_2020_ZT_path = (By.XPATH,"//div[@title='2020']")
    def Select_Year_2020_ZT(self):
        self.find_element(*self.Year_2020_ZT_path).click()
        sleep(1)


    ZT_002_TEST_path = (By.XPATH,"//div[@title='平行记帐测试账套002']")
    def ZT_002_TEST(self):
        self.find_element(*self.ZT_002_TEST_path).click()
        sleep(1)


    SJ_Delete_path = (By.XPATH,"//a[@id='ClkDel3']")
    def SJ_Delete_Button(self):
        self.find_element(*self.SJ_Delete_path).click()
        sleep(1)


    '''初始化科目配置界面用例的元素封装'''
    JF_YJMJ_A_path = (By.XPATH,"//div[@title='一级枚举A']")#一级枚举A
    def JF_YJMJ_A(self):
        self.find_element(*self.JF_YJMJ_A_path).click()
        sleep(1)

    JF_YJMJ_DDDDD_path = (By.XPATH, "//div[@title='DDDDDDD']")  # 一级枚举DDD
    def JF_YJMJ_DDDDD(self):
        self.find_element(*self.JF_YJMJ_DDDDD_path).click()
        sleep(1)

    JF_YJMJ_C_path = (By.XPATH, "//div[@title='一级枚举C']")  # 一级枚举C
    def JF_YJMJ_C(self):
        self.find_element(*self.JF_YJMJ_C_path).click()
        sleep(1)

    JF_YJMJ_B_path = (By.XPATH, "//div[@title='一级枚举B']")  # 一级枚举B
    def JF_YJMJ_B(self):
        self.find_element(*self.JF_YJMJ_B_path).click()
        sleep(1)

    Next_JM_path = (By.XPATH,"//span[@class='pageNext']")
    def Next_JM(self):
        self.find_element(*self.Next_JM_path).click()
        sleep(1)


    Select_1131_path = (By.XPATH,"//div[@title='应收股利']")
    def Select_1131(self):
        self.find_element(*self.Select_1131_path).click()
        sleep(1)

    Select_1146_path = (By.XPATH, "//div[@title='客项部']")
    def Select_1146(self):
        self.find_element(*self.Select_1146_path).click()
        sleep(1)

    Select_1147_path = (By.XPATH, "//div[@title='个项银行']")
    def Select_1147(self):
        self.find_element(*self.Select_1147_path).click()
        sleep(1)

    Select_1148_path = (By.XPATH, "//div[@title='外币核算人民币']")
    def Select_1148(self):
        self.find_element(*self.Select_1148_path).click()
        sleep(1)

    Select_100202_path = (By.XPATH, "//div[@title='现金流量科目2']")
    def Select_100202(self):
        self.find_element(*self.Select_100202_path).click()
        sleep(1)


    Select_1012_path = (By.XPATH, "//div[@title='其他货币资金-外币港元']")
    def Select_1012(self):
        self.find_element(*self.Select_1012_path).click()
        sleep(1)

    Select_1304_path = (By.XPATH, "//div[@title='贷款损失准备']")
    def Select_1304(self):
        self.find_element(*self.Select_1304_path).click()
        sleep(1)
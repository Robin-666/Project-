from selenium.webdriver.common.by import By
from time import sleep
from test_page.Public_method import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class People_Assist(BasePage):


    Assist_title_xpath = (By.XPATH, "//div[@title='辅助核算']")
    def Assist_Button(self):#辅助核算按钮
        self.find_element(*self.Assist_title_xpath).click()

    People_FZHS_path = (By.XPATH,"//li[@id='personAux']/a")
    def People_FZHS_button(self):#人员辅助核算按钮
        self.find_element(*self.People_FZHS_path).click()

    Dep_FZHS_path = (By.XPATH, "//li[@id='departAux']/a/span")
    def Dep_FZHS_button(self):  # 部门辅助核算按钮
        self.find_element(*self.Dep_FZHS_path).click()

    User_Name_Bind_path = (By.XPATH,"//a[@id='autobtn']")
    def User_Name_Bind(self):#按用户名自动绑定
        self.find_element(*self.User_Name_Bind_path).click()


    Msg_Frame_path = (By.XPATH,"//div[@id='rem']")
    def Msg_Frame(self):
        Msg = self.find_element(*self.Msg_Frame_path).text
        sleep(1)
        print(Msg)
        return Msg


    Year_2019_people_path = (By.XPATH,"//select[@id='acctyear']")
    def Year_2019_people(self):
        sel = self.find_element(*self.Year_2019_people_path)
        Select(sel).select_by_value("2019")
        sleep(1)

    def Year_2020_people(self):
        sel = self.find_element(*self.Year_2019_people_path)
        Select(sel).select_by_value("2020")
        sleep(1)

    Peopel_ZT_001_path = (By.XPATH, "//select[@id='acctaccount']")
    def PEOPLE_ZT_001(self):
        sel = self.find_element(*self.Peopel_ZT_001_path)
        Select(sel).select_by_visible_text("001[测试帐套001]")
        sleep(1)

    def PEOPLE_ZT_002(self):
        sel = self.find_element(*self.Peopel_ZT_001_path)
        Select(sel).select_by_visible_text("002[平行记帐测试账套002]")
        sleep(1)

    Bing_state_path = (By.XPATH,"//select[@id='bindingtype']")
    def Bing_state_OK(self):
        sel = self.find_element(*self.Bing_state_path)
        Select(sel).select_by_visible_text("已绑定")
        sleep(1)

    def Bing_state_Not_OK(self):
        sel = self.find_element(*self.Bing_state_path)
        Select(sel).select_by_visible_text("未绑定")
        sleep(1)

    def Bing_state_All(self):
        sel = self.find_element(*self.Bing_state_path)
        Select(sel).select_by_visible_text("全部")
        sleep(1)

    List_Display_two_path = (By.XPATH,"//tbody[@id='list']/tr[1]/td[2]")
    def List_Display_two(self):
        Lab = self.find_element(*self.List_Display_two_path).text
        print(Lab)
        return Lab

    List_Display_four_path = (By.XPATH, "//tbody[@id='list']/tr[1]/td[4]")
    def List_Display_four(self):
        Lab = self.find_element(*self.List_Display_four_path).text
        print(Lab)
        return Lab

    save_frame1_path = (By.XPATH, "//div[@id='layui-layer1']/div[2]/a[1]")
    def Save_frame1(self):
        self.find_element(*self.save_frame1_path).click()
        sleep(1)

    Not_save_frame1_path = (By.XPATH, "//div[@id='layui-layer1']/div[2]/a[2]")
    def Not_Save_frame1(self):
        self.find_element(*self.Not_save_frame1_path).click()
        sleep(1)

    All_select_button_path = (By.XPATH,"//div[@id='centers']/div/div[3]/div/table/thead/tr/th[1]/div/input")
    def All_Select_Button(self):
        self.find_element(*self.All_select_button_path).click()
        sleep(1)


    Clear_Button_path = (By.XPATH,"//a[@id='delbtn']")
    def Clear_Button(self):
        self.find_element(*self.Clear_Button_path).click()
        sleep(1)

    All_Display_path = (By.XPATH,"//table[@id='mytable']")
    def All_Display(self):
        Lab = self.find_element(*self.All_Display_path).text
        print("列表显示区显示数据为%s空"%Lab)
        return Lab



    OA_people_BGSRY_path = (By.XPATH,"//div[@title = '办公室人员A']")
    def OA_people_A(self):
        self.find_element(*self.OA_people_BGSRY_path).click()
        sleep(1)

    ERP_people_006_path = (By.XPATH, "//div[@title = '英特']")
    def ERP_people_006(self):
        self.find_element(*self.ERP_people_006_path).click()
        sleep(1)

    Save_Bing_path = (By.XPATH,"//a[@id='addbtn']")#保存绑定
    def Save_Bind(self):
        self.find_element(*self.Save_Bing_path).click()

    OA_people_BGSKY1_path = (By.XPATH, "//div[@title = '办公室科员1']")
    def OA_people_BGSKY1(self):
        self.find_element(*self.OA_people_BGSKY1_path).click()
        sleep(1)

    OA_people_BGSKY2_path = (By.XPATH, "//div[@title = '办公室科员2']")
    def OA_people_BGSKY2(self):
        self.find_element(*self.OA_people_BGSKY2_path).click()
        sleep(1)

    OA_people_BGSKY3_path = (By.XPATH, "//div[@title = '办公室科员3']")
    def OA_people_BGSKY3(self):
        self.find_element(*self.OA_people_BGSKY3_path).click()
        sleep(1)

    ERP_people_ZS_path = (By.XPATH, "//div[@title = '张三']")
    def ERP_people_ZS(self):
        self.find_element(*self.ERP_people_ZS_path).click()
        sleep(1)

    ERP_people_LS_path = (By.XPATH, "//div[@title = '李四']")
    def ERP_people_LS(self):
        self.find_element(*self.ERP_people_LS_path).click()
        sleep(1)

    OA_people_BGSZR_path = (By.XPATH, "//div[@title = '办公室主任']")
    def OA_people_BGSZR(self):
        self.find_element(*self.OA_people_BGSZR_path).click()
        sleep(1)

    OA_CXTJ_path = (By.XPATH,"//div[@id='searchOaInfo']/p")
    def OA_CXTJ(self):
        self.find_element(*self.OA_CXTJ_path).click()
        sleep(1)

    OA_CXTJ_Name_path = (By.XPATH, "//div[@id='rightbox']/div[2]/div/div/div[2]/p[2]")
    def OA_CXTJ_Name(self):
        self.find_element(*self.OA_CXTJ_Name_path).click()
        sleep(1)

    OA_CXTJ_YWY_BM_path = (By.XPATH, "//div[@id='rightbox']/div[2]/div/div/div[2]/p[3]")
    def OA_CXTJ_YWY_BM(self):
        self.find_element(*self.OA_CXTJ_YWY_BM_path).click()
        sleep(1)

    OA_CXTJ_YWY_name_path = (By.XPATH, "//div[@id='rightbox']/div[2]/div/div/div[2]/p[4]")
    def OA_CXTJ_YWY_name(self):
        self.find_element(*self.OA_CXTJ_YWY_name_path).click()
        sleep(1)

    OA_Name_input_path = (By.XPATH,"//input[@id='searchOaInput']")#OA用户名输入框
    def OA_Name_input_Send_key(self,key):
        self.find_element(*self.OA_Name_input_path).send_keys(key)
        sleep(1)

    def Clear_OA_Name_input_Send_key(self):
        self.find_element(*self.OA_Name_input_path).clear()
        sleep(1)

    OA_Search_OA_NAME_path = (By.XPATH,"//p[@id='clkSearchOa']/i")
    def OA_Search_OA_NAME(self):
        self.find_element(*self.OA_Search_OA_NAME_path).click()
        sleep(0.5)

    ERP_CXTJ_path = (By.XPATH, "//div[@id='searchErpInfo']/p")
    def ERP_CXTJ(self):#ERP查询条件
        self.find_element(*self.ERP_CXTJ_path).click()
        sleep(1)

    ERP_CXTJ_YWY_BM_path = (By.XPATH, "//div[@id='rightbox']/div[3]/div/div/div[2]/p[2]")
    def ERP_CXTJ_YWY_BM(self):#ERP业务员编码
        self.find_element(*self.ERP_CXTJ_YWY_BM_path).click()
        sleep(1)

    ERP_CXTJ_YWY_name_path = (By.XPATH, "//div[@id='rightbox']/div[3]/div/div/div[2]/p[3]")
    def ERP_CXTJ_YWY_name(self):  # ERP业务员名称
        self.find_element(*self.ERP_CXTJ_YWY_name_path).click()
        sleep(1)

    ERP_input_path = (By.XPATH,"//input[@id='searchErpInput']")
    def ERP_input_Send_key(self,key):
        self.find_element(*self.ERP_input_path).send_keys(key)
        sleep(1)

    def Clear_ERP_input_Send_key(self):
        self.find_element(*self.ERP_input_path).clear()
        sleep(1)


    ERP_Search_Button_path = (By.XPATH, "//p[@id='clkSearchErp']/i")
    def ERP_Search_button(self):
        self.find_element(*self.ERP_Search_Button_path).click()
        sleep(0.5)


    ERP_Data_Display_path = (By.XPATH,"//div[@id='east_center']/div/div[6]/div/span/span[1]")
    def ERP_Data_Display(self):
        Lab = self.find_element(*self.ERP_Data_Display_path).text
        print(Lab)
        return Lab

    DW_input_text_path = (By.XPATH,"//input[@id='search_input']")
    def DW_input_text(self,key):
        self.find_element(*self.DW_input_text_path).send_keys(key)
        sleep(1)

    DW_Button_path = (By.XPATH,"//a[@id='search_btn']")
    def DW_Button(self):
        self.find_element(*self.DW_Button_path).click()

    def Clear_DW_input_text(self):
        self.find_element(*self.DW_input_text_path).clear()

    Unit_C_path = (By.XPATH,"//span[@id='mytree_56_span']")
    def Unit_C(self):
        Lab = self.find_element(*self.Unit_C_path).text
        print(Lab)#单位C
        return Lab

    Administrator_path = (By.XPATH, "//span[@id='mytree_3_span']")
    def Administrator(self):
        Lab = self.find_element(*self.Administrator_path).text
        print(Lab)  # 办公室 administrator  clearUp1
        return Lab

    prevpage_path = (By.XPATH,"//button[@id='prevpage']")
    def prevpage(self):
        self.find_element(*self.prevpage_path).click()
        sleep(1)

    nextpage_path = (By.XPATH,"//button[@id='nextpage']")
    def nextpage(self):
        self.find_element(*self.nextpage_path).click()
        sleep(1)


    Clear_Up_path = (By.XPATH,"//a[@id='clearUp1']")
    def Clear_Up(self):
        Lab = self.find_element(*self.Clear_Up_path).text
        print(Lab)
        return Lab#科目配置-整理按钮


    Year_End_path = (By.XPATH,"//a[@id='YearEnd']")
    def Year_End(self):
        Lab = self.find_element(*self.Year_End_path).text
        print(Lab)
        return Lab


    JF_MJ_DDDD_path = (By.XPATH,"//table[@title='Robin-第二章']/tbody/tr/td[2]/a")
    def JF_MJ_DDDD(self):
        self.find_element(*self.JF_MJ_DDDD_path).click()
        sleep(1)

    JF_MJ_Button_path = (By.XPATH,"//section[@class='formson_0144']/table/tbody/tr[2]/td[2]/"
                                  "div/section/div/div/div/div/input")
    def JF_MJ_Button(self):
        self.find_element(*self.JF_MJ_Button_path).click()
        sleep(1)

    JF_KMBM_Text_Value_path = (By.XPATH,"//section[@class='formson_0144']/table/tbody/tr[2]/td[4]/"
                                        "div/div/section/div[2]/div")
    def JF_KMBM_Text_Value(self):
        Lab = self.find_element(*self.JF_KMBM_Text_Value_path).text
        print("此时Lab的值:%s"%Lab)
        return Lab

    JF_KM_name_Text_Value_path = (By.XPATH, "//section[@class='formson_0144']/table/tbody/tr[2]/td[5]/"
                                         "div/div/section/div[2]/div")

    def JF_KM_name_Text_Value(self):
        Lab = self.find_element(*self.JF_KM_name_Text_Value_path).text
        print("此时Lab的值:%s"%Lab)
        return Lab

    JF_BXJE_Text_Value_path = (By.XPATH, "//section[@class='formson_0144']/table/tbody/tr[2]/td[3]/"
                                            "div/section/div[2]/div/div[2]/input")
    def JF_BXJE_Text_Value(self,key):
        self.find_element(*self.JF_BXJE_Text_Value_path).send_keys(key)
        sleep(1)
        #借方的报销金额


    JF_Select_MJ_DDDD_path =  (By.XPATH,"//div[@class='cap4-scontent']/div[5]/div")
    def JF_Select_MJ_DDDD(self):#枚举DDDD
        self.find_element(*self.JF_Select_MJ_DDDD_path).click()
        sleep(1)

    JF_Select_MJ_C_path = (By.XPATH, "//div[@class='cap4-scontent']/div[4]/div")
    def JF_Select_MJ_C(self):  # 枚举一级C
        self.find_element(*self.JF_Select_MJ_C_path).click()
        sleep(1)

    JF_Select_MJ_B_path = (By.XPATH, "//div[@class='cap4-scontent']/div[3]/div")
    def JF_Select_MJ_B(self):  # 枚举一级B
        self.find_element(*self.JF_Select_MJ_B_path).click()
        sleep(1)

    JF_Select_MJ_A_path = (By.XPATH, "//div[@class='cap4-scontent']/div[2]/div")
    def JF_Select_MJ_A(self):  # 枚举一级A
        self.find_element(*self.JF_Select_MJ_A_path).click()
        sleep(1)

    DF_KMBM_Text_Value_path = (By.XPATH, "//section[@class='formson_0145']/table/tbody/tr[2]/td[4]/"
                                         "div/div/section/div[2]/div")

    def DF_KMBM_Text_Value(self):#贷方科目编码
        Lab = self.find_element(*self.DF_KMBM_Text_Value_path).text
        print("此时Lab的值:%s" % Lab)
        return Lab

    DF_KM_name_Text_Value_path = (By.XPATH, "//section[@class='formson_0145']/table/tbody/tr[2]/td[5]/"
                                         "div/div/section/div[2]/div")
    def DF_KM_name_Text_Value(self):  # 贷方科目名称
        Lab = self.find_element(*self.DF_KM_name_Text_Value_path).text
        print("此时Lab的值:%s" % Lab)
        return Lab

    DF_MJ_Button_path = (By.XPATH, "//section[@class='formson_0145']/table/tbody/tr[2]/td[2]/"
                                   "div/section/div[2]/div/div/div/input")
    def DF_MJ_Button(self):
        self.find_element(*self.DF_MJ_Button_path).click()
        sleep(1)

    DF_BXJE_Text_Value_path = (By.XPATH, "//section[@class='formson_0145']/table/tbody/tr[2]/td[3]/"
                                         "div/section/div[2]/div/div[2]/input")

    def DF_BXJE_Text_Value(self, key):
        self.find_element(*self.DF_BXJE_Text_Value_path).send_keys(key)
        sleep(1)
        # 贷方的支付金额


    DF_Select_MJ_DDDD_path = (By.XPATH, "//div[contains(@id,'field0029')]/div[5]/div")
    def DF_Select_MJ_DDDD(self):  # 枚举DDDD
        self.find_element(*self.DF_Select_MJ_DDDD_path).click()
        sleep(1)

    DF_Select_MJ_C_path = (By.XPATH, "//div[contains(@id,'field0029')]/div[4]/div")
    def DF_Select_MJ_C(self):  # 一级C
        self.find_element(*self.DF_Select_MJ_C_path).click()
        sleep(1)

    DF_Select_MJ_B_path = (By.XPATH, "//div[contains(@id,'field0029')]/div[3]/div")
    def DF_Select_MJ_B(self):  # 一级B
        self.find_element(*self.DF_Select_MJ_B_path).click()
        sleep(1)

    Select_People_icon_path = (By.XPATH,"//div[@class='icon CAP cap-icon-xuanren']")
    def Select_People_icon(self):
        self.find_element(*self.Select_People_icon_path).click()
        sleep(1)

    Select_CXB_path = (By.XPATH,"//select[@id='memberDataBody']/option[3]")
    def Select_CXB(self):
        self.find_element(*self.Select_CXB_path).click()
        sleep(1)

    Select_Right_icon_path = (By.XPATH,"//span[@class='select_selected']")
    def Select_Right_icon(self):
        self.find_element(*self.Select_Right_icon_path).click()
        sleep(1)

    Form_Send_path = (By.XPATH,"//a[@id='sendId']")
    def Form_Send(self):
        self.find_element(*self.Form_Send_path).click()
        sleep(1)

    Select_Wait_Do_path = (By.XPATH,"//div[@title='待办事项']/div[2]")
    def Select_Wait_Do(self):#鼠标悬浮到待办事项
        move = self.find_element(*self.Select_Wait_Do_path)  # 鼠标悬停
        ActionChains(self.driver).move_to_element(move).perform()
        sleep(1)
        self.driver.find_element(*self.Select_Wait_Do_path).click()
        sleep(1)


    All_Wait_Do_path = (By.XPATH,"//div[@id='allPendingNum']")
    def All_Wait_Do(self):
        self.find_element(*self.All_Wait_Do_path).click()


    Wait_Do_List_Display_Button_path = (By.XPATH,"//tbody[@id='list']/tr[1]/td[2]/div/span/span")
    def Wait_Do_List_Display_Button(self):
        self.find_element(*self.Wait_Do_List_Display_Button_path).click()
        sleep(1)

    Agree_Button_path = (By.XPATH,"//input[@title = '同意']")
    def Agree_Button(self):
        self.find_element(*self.Agree_Button_path).click()
        sleep(1)


    Span_Title_path = (By.XPATH,"//span[@title = '1147[个项银行]']")
    def Span_Title(self):
        self.find_element(*self.Span_Title_path).click()
        sleep(1)

    Span_Title_1131_path = (By.XPATH, "//span[@title = '1131[应收股利]']")
    def Span_Title_1131(self):
        self.find_element(*self.Span_Title_1131_path).click()
        sleep(1)

    PZ_Display_path = (By.XPATH,"//div[@class='bottomdiv']/div[2]/div/span")#凭证显示业务员的区域
    def PZ_Display(self):
        Lab = self.find_element(*self.PZ_Display_path).text
        print("此时Lab的值:%s" % Lab)
        return Lab

    Dep_BGS_path = (By.XPATH,"//div[@title = '办公室']")
    def Dep_BGS(self):
        self.find_element(*self.Dep_BGS_path).click()
        sleep(1)

    Dep_ERP_TestDep_path = (By.XPATH, "//div[@title = '测试部']")
    def Dep_ERP_TestDep(self):
        self.find_element(*self.Dep_ERP_TestDep_path).click()
        sleep(1)



    Dialog_OK_Button_path = (By.XPATH,"//a[@id='layui-layer-btn-ok']")
    def Dialog_OK_Button(self):
        self.find_element(*self.Dialog_OK_Button_path).click()
        sleep(1)

    Dep_ZHK_path = (By.XPATH, "//div[@title = '综合科']")
    def Dep_ZHK(self):
        self.find_element(*self.Dep_ZHK_path).click()
        sleep(1)

    Dep_ZHS_path = (By.XPATH, "//div[@title = '综合司']")
    def Dep_ZHS(self):
        self.find_element(*self.Dep_ZHS_path).click()
        sleep(1)

    Dep_TFS_path = (By.XPATH, "//div[@title = '条法司']")
    def Dep_TFS(self):
        self.find_element(*self.Dep_TFS_path).click()
        sleep(1)

    Dep_GWY_path = (By.XPATH, "//div[@title = '国务院']")
    def Dep_GWY(self):
        self.find_element(*self.Dep_GWY_path).click()
        sleep(1)

    Dep_JSB_path = (By.XPATH, "//div[@title = '技术部']")
    def Dep_JSB(self):
        self.find_element(*self.Dep_JSB_path).click()
        sleep(1)

    Dep_JCS_path = (By.XPATH,"//span[@id='mytree_6_span']")
    def Dep_JCS(self):
        self.find_element(*self.Dep_JCS_path).click()
        sleep(1)

    CXB_path = (By.XPATH,"//div[@title='崔雄B']")
    def CXB(self):
        self.find_element(*self.CXB_path).click()
        sleep(1)

    CXD_path = (By.XPATH, "//div[@title='崔雄D']")
    def CXD(self):
        self.find_element(*self.CXD_path).click()
        sleep(1)














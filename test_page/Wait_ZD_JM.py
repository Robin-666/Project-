from selenium.webdriver.common.by import By
from time import sleep
from test_page.Public_method import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

class Wait_ZD(BasePage):


    Wait_JM_Button_path = (By.XPATH,"//div[@class='myheader']/div[1]/i/span")
    def Wait_JM_Button(self):#待制单
        self.find_element(*self.Wait_JM_Button_path).click()
        sleep(1)

    Wait_YZD_Button_path = (By.XPATH, "//div[@class='myheader']/div[2]/i/span")
    def Wait_YZD_Button(self):  # 已制单
        self.find_element(*self.Wait_YZD_Button_path).click()
        sleep(1)

    Select_ZT_path = (By.XPATH,"//span[@title = '请选择账套配置...']")
    def Select_ZT_Button(self):
        self.find_element(*self.Select_ZT_path).click()
        sleep(1)

    Select_BD_path = (By.XPATH, "//span[@title = '请选择表单...']")
    def Select_BD_Button(self):
        self.find_element(*self.Select_BD_path).click()
        sleep(1)

    Select_Robin_path = (By.XPATH, "//div[@title = 'Robin-第二章']")
    def Select_Robin_Button(self):
        self.find_element(*self.Select_Robin_path).click()
        sleep(1)

    Select_C2_path = (By.XPATH, "//div[@title = 'C2测试']")
    def Select_C2_Button(self):
        self.find_element(*self.Select_C2_path).click()
        sleep(1)

    Select_R2_path = (By.XPATH, "//div[@title = 'Robin-1']")
    def Select_R2_Button(self):
        self.find_element(*self.Select_R2_path).click()
        sleep(1)


    Select_2020_ZT_path = (By.XPATH,"//div[@title='2020——First_SQ_List']")
    def Select_2020_ZT(self):
        self.find_element(*self.Select_2020_ZT_path).click()
        sleep(2)

    Select_New_LB_ZT_path = (By.XPATH, "//div[@title='新建账套萝卜1']")
    def Select_New_LB_ZT(self):
        self.find_element(*self.Select_New_LB_ZT_path).click()
        sleep(2)

    Select_123_ZT_path = (By.XPATH, "//div[@title='123']")
    def Select_123_ZT(self):
        self.find_element(*self.Select_123_ZT_path).click()
        sleep(2)

    Select_11111_ZT_path = (By.XPATH, "//div[@title='111111']")
    def Select_111111_ZT(self):
        self.find_element(*self.Select_11111_ZT_path).click()
        sleep(2)

    Select_U8_ZT_path = (By.XPATH, "//div[@title='U8-001-A']")
    def Select_U8_ZT(self):
        self.find_element(*self.Select_U8_ZT_path).click()
        sleep(2)


    Select_Year_path = (By.XPATH,"//select[@id='clkYear']")
    def Select_Year_2019(self):
        sel = self.find_element(*self.Select_Year_path)
        Select(sel).select_by_value("2019")
        sleep(1)

    def Select_Year_2020(self):
        sel = self.find_element(*self.Select_Year_path)
        Select(sel).select_by_value("2020")
        sleep(1)

    Month_3_path = (By.XPATH,"//select[@id='clkMonth']/option[4]")
    def Month_3(self):
        self.find_element(*self.Month_3_path).click()
        sleep(1)

    List_1_path = (By.XPATH,"//tbody[@id='list']/tr[1]/td[1]/div/input")
    def List_1(self):
        self.find_element(*self.List_1_path).click()
        sleep(1)

    List_2_path = (By.XPATH, "//tbody[@id='list']/tr[2]/td[1]/div/input")
    def List_2(self):
        self.find_element(*self.List_2_path).click()
        sleep(1)

    Button_ZZPZ_path = (By.XPATH,"//button[@id='making']")
    def Button_ZZPZ(self):#凭证制单
        self.find_element(*self.Button_ZZPZ_path).click()
        sleep(1)


    Button_BZD_path = (By.XPATH, "//button[@id='noMaking']")
    def Button_BZD(self):#不制单
        self.find_element(*self.Button_BZD_path).click()
        sleep(1)

    BZD_Text_path = (By.XPATH,"//div[@id='_main']/center/textarea")
    def BZD_Text(self,key):
        self.find_element(*self.BZD_Text_path).send_keys(key)

    Only_One_Button_path = (By.XPATH,"//input[@id='onlyOne']")
    def Only_One_Button(self):
        self.find_element(*self.Only_One_Button_path).click()
        sleep(1)






    Advanced_Query_path = (By.XPATH,"//a[@id='highQuery']")
    def Advanced_Query(self):#高级查询
        self.find_element(*self.Advanced_Query_path).click()
        sleep(1)


    XT_Time1_path = (By.XPATH,"//form[@id='addForm']/table/tbody/tr[1]/td/span[1]/span")
    def XT_Time1(self):
        self.find_element(*self.XT_Time1_path).click()
        sleep(1)

    XT_Time2_path = (By.XPATH, "//form[@id='addForm']/table/tbody/tr[1]/td/span[3]/span")
    def XT_Time2(self):
        self.find_element(*self.XT_Time2_path).click()
        sleep(1)

    select_10_Datatime_path = (By.XPATH,"//div[@class='calendar miniCalendar']/table/tbody/tr[2]/td[3]")
    def select_10_Datatime(self):
        self.find_element(*self.select_10_Datatime_path).click()
        sleep(1)

    select_11_Datatime_path = (By.XPATH, "//div[@class='calendar miniCalendar']/table/tbody/tr[2]/td[4]")
    def select_11_Datatime(self):
        self.find_element(*self.select_11_Datatime_path).click()
        sleep(1)

    Span_OK_path = (By.XPATH,"//span[@class='common_button common_button_emphasize margin_r_5']")
    def Span_OK(self):
        self.find_element(*self.Span_OK_path).click()
        sleep(1)

    Select_people_button_path = (By.XPATH,"//div[@align='center']")
    def Select_people_button(self):
        self.find_element(*self.Select_people_button_path).click()
        sleep(1)

    Select_CXB_people_path = (By.XPATH,"//option[contains(@title,'崔雄B')]")
    def Select_CXB_people(self):
        self.find_element(*self.Select_CXB_people_path).click()
        sleep(1)

    Select_JCS_A_people_path = (By.XPATH, "//option[contains(@title,'监查室人员A')]")
    def Select_JCS_A_people(self):
        self.find_element(*self.Select_JCS_A_people_path).click()
        sleep(1)

    Clear_Select_people_input_path = (By.XPATH,"//input[@id='ab_senderno-Temp']")
    def Clear_Select_people_input(self):
        self.find_element(*self.Clear_Select_people_input_path).clear()
        sleep(1)

    Advanced_Query_Input_path = (By.XPATH,"//input[@id='ab_title-C']")
    def Advanced_Query_Input(self,key):
        self.find_element(*self.Advanced_Query_Input_path).send_keys(key)
        sleep(1)

    def Clear_Advanced_Query_Input(self):
        self.find_element(*self.Advanced_Query_Input_path).clear()
        sleep(1)

    Select_Right_Button_path = (By.XPATH,"//span[@class='select_selected']")
    def Select_Right_Button(self):
        self.find_element(*self.Select_Right_Button_path).click()
        sleep(1)

    Select_Left_Button_path = (By.XPATH, "//span[@class='select_unselect']")
    def Select_Left_Button(self):
        self.find_element(*self.Select_Left_Button_path).click()
        sleep(1)


    Select_CXA_1_path = (By.XPATH,"//div[@title='综合科']/a")
    def Select_CXA_1(self):
        self.find_element(*self.Select_CXA_1_path).click()
        sleep(1)

    Select_CXA_people_path = (By.XPATH, "//option[contains(@title,'崔雄A')]")
    def Select_CXA_people(self):
        self.find_element(*self.Select_CXA_people_path).click()
        sleep(1)


    '''凭证制单界面'''

    Button_LL_path = (By.XPATH,"//button[@id='cash']")
    def Button_LL(self):
        self.find_element(*self.Button_LL_path).click()
        sleep(1)

    Button_Save_path = (By.XPATH, "//button[@id='savepz']")
    def Button_Save(self):
        sleep(3)
        self.find_element(*self.Button_Save_path).click()
        sleep(2)

    Quit_Button_path = (By.XPATH, "//div[@id='north']/button[3]")
    def Quit_Button(self):
        sleep(3)
        self.find_element(self.Quit_Button_path).click()
        sleep(1)

    Header_path = (By.XPATH,"//div[@class='myhead']/p")
    def Header(self):
        Lab = self.find_element(*self.Header_path).text
        print(Lab)
        return Lab



    '''已制单界面'''
    OK_ZD_JM_path = (By.XPATH,"//div[@class='myheader']/div[2]/span")
    def OK_ZD_JM(self):
        self.find_element(*self.OK_ZD_JM_path).click()
        sleep(1)

    Look_PZ_path = (By.XPATH,"//div[@id='mytoolbar1toolbox']/a[3]")
    def Look_PZ(self):#查看凭证
        self.find_element(*self.Look_PZ_path).click()
        sleep(1)

    Quit_Button_1_path = (By.XPATH, "//div[@id='north']/button[4]")
    def Quit_Button_1(self):
        sleep(3)
        self.find_element(self.Quit_Button_1_path).click()
        sleep(1)


    Up_data_Button_path = (By.XPATH,"//a[@id='tidy']")
    def Up_data_Button(self):
        self.find_element(*self.Up_data_Button_path).click()
        sleep(1)

    SG_ZD_JM_path = (By.XPATH, "//div[@class='myheader']/div[5]/span")
    def SG_ZD_JM(self):
        self.find_element(*self.SG_ZD_JM_path).click()
        sleep(1)




    '''不制单界面'''
    Not_ZD_JM_path = (By.XPATH, "//div[@class='myheader']/div[3]/span")
    def Not_ZD_JM(self):
        self.find_element(*self.Not_ZD_JM_path).click()
        sleep(1)

    Not_ZD_MX_path = (By.XPATH,"//a[@id='notVoucherDetail']")#不制单明细
    def Not_ZD_MX(self):
        self.find_element(*self.Not_ZD_MX_path).click()
        sleep(1)

    List_Display_4_path = (By.XPATH,"//tbody[@id='list']/tr[1]/td[4]")
    def List_Display_4(self):
        Lab = self.find_element(*self.List_Display_4_path).text
        print(Lab)
        return Lab

    List_Display_5_path = (By.XPATH, "//tbody[@id='list']/tr[1]/td[5]")
    def List_Display_5(self):
        Lab = self.find_element(*self.List_Display_5_path).text
        print(Lab)
        return Lab

    Re_ZD_Button_path = (By.XPATH,"//a[@id='yesMaking']")
    def Re_ZD_Button(self):
        self.find_element(*self.Re_ZD_Button_path).click()
        sleep(1)

    '''手工填单界面'''
    SG_ZD_JM_New_Add_Button_path = (By.XPATH,"//a[@id='making']")
    def SG_ZD_JM_New_Add_Button(self):
        self.find_element(*self.SG_ZD_JM_New_Add_Button_path).click()
        sleep(1)



    Input_First_1_text_path = (By.XPATH,"//div[@id='flTalbe']/table/tbody/tr[1]/td[2]")
    def Double_Click_Input_First(self):#双击操作
        input_text = self.find_element(*self.Input_First_1_text_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()
        self.driver.implicitly_wait(10)

    Input_First_1_text_ZY_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[1]/td[2]/input")
    def Input_First_1_text_ZY(self,key):#第一行输入摘要信息
        self.find_element(*self.Input_First_1_text_ZY_path).send_keys(key)
        sleep(1)

    Input_First_2_text_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[1]/td[3]")
    def Double_Click_Input_First_2(self):  # 双击操作
        input_text = self.find_element(*self.Input_First_2_text_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()

    Input_First_2_KM_Button_path = (By.XPATH,"//i[@id='kmobjicon0']")
    def Input_First_2_KM_Button(self):
        self.find_element(*self.Input_First_2_KM_Button_path).click()
        sleep(1)

    Input_Two_2_KM_Button_path = (By.XPATH, "//i[@id='kmobjicon1']")
    def Input_Two_2_KM_Button(self):
        self.find_element(*self.Input_Two_2_KM_Button_path).click()
        sleep(1)


    Select_6001_path = (By.XPATH,"//div[@title='主营业务收入']")
    def Select_6001(self):
        self.find_element(*self.Select_6001_path).click()
        sleep(1)

    Select_6031_path = (By.XPATH, "//div[@title='保费收入']")
    def Select_6031(self):
        self.find_element(*self.Select_6031_path).click()
        sleep(1)

    JF_RMB_path = (By.XPATH,"//div[@id='flTalbe']/table/tbody/tr[1]/td[7]")#借方金额
    def JF_RMB(self):
        input_text = self.find_element(*self.JF_RMB_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()

    Input_JF_RMB_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[1]/td[7]/input")  # 借方金额
    def Input_JF_RMB(self,key):
        self.find_element(*self.Input_JF_RMB_path).send_keys(key)
        sleep(1)

    Input_Two_2_text_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[2]/td[2]")
    def Double_Click_Input_Two(self):  # 双击操作
        input_text = self.find_element(*self.Input_Two_2_text_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()
        self.driver.implicitly_wait(10)

    Input_Two_2_text_ZY_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[2]/td[2]/input")
    def Input_Two_2_text_ZY(self, key):  # 第二行输入摘要信息
        self.find_element(*self.Input_Two_2_text_ZY_path).send_keys(key)
        sleep(1)

    Input_Two_2__2_text_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[2]/td[3]")
    def Double_Click_Input_Two_2(self):  # 双击操作
        input_text = self.find_element(*self.Input_Two_2__2_text_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()

    DF_RMB_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[2]/td[8]")  # 贷方金额
    def DF_RMB(self):
        input_text = self.find_element(*self.DF_RMB_path)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(input_text).perform()

    Input_DF_RMB_path = (By.XPATH, "//div[@id='flTalbe']/table/tbody/tr[2]/td[8]/input")  # 贷方金额
    def Input_DF_RMB(self,key):
        self.find_element(*self.Input_DF_RMB_path).send_keys(key)

    Data_time_path = (By.XPATH,"//input[@id='billdate']")
    def Data_time(self,key):
        self.find_element(*self.Data_time_path).send_keys(key)
        sleep(1)

    def Call_Data_time(self):
        a = time.strftime("%Y-%m-%d")
        return a

    def Clear_Data_time(self):
        self.find_element(*self.Data_time_path).clear()
        sleep(1)

    Sel_PZZ_C_path = (By.XPATH,"//select[@id='voucherType']")
    def Sel_PZZ_C(self):
        sel = self.find_element(*self.Sel_PZZ_C_path)
        Select(sel).select_by_value("财")
        sleep(1)

    def Clear_Sel_PZZ(self):
        self.find_element(*self.Sel_PZZ_C_path).clear()
        sleep(1)

    def Sel_PZZ_YQ(self):
        sel = self.find_element(*self.Sel_PZZ_C_path)
        Select(sel).select_by_value("有权")
        sleep(1)

    def Sel_Start(self):
        sel = self.find_element(*self.Sel_PZZ_C_path)
        Select(sel).select_by_value("请选择记账类型")
        sleep(1)

    Sel_Account_path = (By.XPATH,"//select[@id='acctPeriod']")#会计期间
    def Sel_Account_1(self):
        sel = self.find_element(*self.Sel_Account_path)
        Select(sel).select_by_value("1")
        sleep(1)

    def Sel_Account_All(self):
        sel = self.find_element(*self.Sel_Account_path)
        Select(sel).select_by_visible_text("全部")
        sleep(1)

    def Sel_Account_2(self):
        sel = self.find_element(*self.Sel_Account_path)
        Select(sel).select_by_value("2")
        sleep(1)


    def Sel_Account_3(self):
        sel = self.find_element(*self.Sel_Account_path)
        Select(sel).select_by_value("3")
        sleep(1)

    Up_Data_info_path = (By.XPATH,"//a[@id='tidy']")
    def Up_Data_info(self):
        self.find_element(*self.Up_Data_info_path).click()
        sleep(1)


    '''凭证查询界面'''
    PZ_Check_JM_path = (By.XPATH, "//div[@class='myheader']/div[4]/span")
    def PZ_Check_JM(self):
        self.find_element(*self.PZ_Check_JM_path).click()
        sleep(1)

    ZT_PZ_Input_Button_path = (By.XPATH,"//input[@id='showAcctAlias']")
    def ZT_PZ_Input_Button(self):
        self.find_element(*self.ZT_PZ_Input_Button_path).click()
        sleep(1)

    Condition_Check_path = (By.XPATH,"//div[@id='north']/div/table/tbody/tr/td[1]/a")#条件查询
    def Condition_Check_Button(self):
        self.find_element(*self.Condition_Check_path).click()
        sleep(1)

    Form_Select_Button_path = (By.XPATH,"//input[@id='formNames']")
    def Form_Select_Button(self):
        self.find_element(*self.Form_Select_Button_path).click()
        sleep(1)

    def Clear_Form_Select_Button(self):#表单
        self.find_element(*self.Form_Select_Button_path).clear()
        sleep(1)


    DR_PZ_path = (By.XPATH,"//div[@title='发起者科目配置带入凭证']")#带入凭证
    def DR_PZ(self):
        self.find_element(*self.DR_PZ_path).click()
        sleep(1)


    Unit_MJ_path = (By.XPATH, "//div[@title='测试科目配置-单位枚举']")  #
    def Unit_MJ(self):
        self.find_element(*self.Unit_MJ_path).click()
        sleep(1)


    PZ_Text_XL_path = (By.XPATH,"//select[@id='voucherType']")
    def PZ_Text_XL(self):#凭证字下拉
        sel = self.find_element(*self.PZ_Text_XL_path)
        Select(sel).select_by_visible_text("请选择记账类型")
        sleep(1)

    ZD_People_path = (By.XPATH,"//input[@id='makingNms']")
    def Clear_ZD_People(self):#制单人
        self.find_element(*self.ZD_People_path).clear()

    def Click_ZD_People(self):
        self.find_element(*self.ZD_People_path).click()
        sleep(1)



    Synergy_title_path = (By.XPATH, "//input[@id='theTitle']")
    def Clear_Synergy_title(self):  # 协同标题
        self.find_element(*self.Synergy_title_path).clear()

    def Synergy_title_Send_Key(self,key):
        self.find_element(*self.Synergy_title_path).send_keys(key)
        sleep(1)


    Disest_infor_path = (By.XPATH, "//input[@id='digest']")
    def Clear_Disest_infor(self):  # 摘要信息
        self.find_element(*self.Disest_infor_path).clear()

    def Disest_infor_Send_Key(self,key):
        self.find_element(*self.Disest_infor_path).send_keys(key)
        sleep(1)


    def PZ_Text_YQ(self):#有权
        sel = self.find_element(*self.PZ_Text_XL_path)
        Select(sel).select_by_visible_text("有权")
        sleep(1)

    def PZ_Text_CAI(self):#财
        sel = self.find_element(*self.PZ_Text_XL_path)
        Select(sel).select_by_visible_text("财")
        sleep(1)

    def PZ_Text_JI(self):#记
        sel = self.find_element(*self.PZ_Text_XL_path)
        Select(sel).select_by_visible_text("记")
        sleep(1)

    def PZ_Text_BY(self):#必有
        sel = self.find_element(*self.PZ_Text_XL_path)
        Select(sel).select_by_visible_text("必有")
        sleep(1)

    PZ_Min_Number_path = (By.XPATH,"//input[@id='minVoucherNo']")
    def PZ_Min_Number(self,key):#凭证号
        self.find_element(*self.PZ_Min_Number_path).send_keys(key)
        sleep(1)

    def Clear_PZ_Min_Number(self):
        self.find_element(*self.PZ_Min_Number_path).clear()
        sleep(1)


    PZ_Max_Number_path = (By.XPATH, "//input[@id='maxVoucherNo']")
    def PZ_Max_Number(self, key):  # 凭证号
        self.find_element(*self.PZ_Max_Number_path).send_keys(key)
        sleep(1)

    def Clear_PZ_Max_Number(self):
        self.find_element(*self.PZ_Max_Number_path).clear()
        sleep(1)


    JCS_KM_path = (By.XPATH,"//div[@title='监查室']/a")
    def JCS_KM(self):
        self.find_element(*self.JCS_KM_path).click()
        sleep(1)

























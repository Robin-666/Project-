from selenium.webdriver.common.by import By
from test_page.Public_method import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class ERP_JM(BasePage):
    # 必填为开状态
    # Must_on_path = (By.XPATH,"//table[@cellspacing='0px']/tbody/tr[1]/td/div/input")
    Must_on_path = (By.XPATH,"//div[@id='bottom']/form/table/tbody/tr[1]/td/div/input")
    def ERP_JM_ON(self):
        self.find_element(*self.Must_on_path).click()
        # ON_state = self.find_element(*self.Must_on).is_selected()
        # print("此时按钮的状态",ON_state)
        # if ON_state:  # 返回True时，就执行下面的语句
        #     print("被选中", " ", ON_state)
        # else:
        #     print("没有被选中", ON_state)


    OK_button_path = (By.XPATH,"//a[@id='btnok']")
    def OK_button(self):
        self.find_element(*self.OK_button_path).click()

    ERP_info_PATH = (By.XPATH, "//div[@class='dialog_main_content_html ']")
    def ERP_Dialog(self):
        Msg = self.find_element(*self.ERP_info_PATH).text
        sleep(1)
        print(Msg)
        return Msg

    ERP_OK_Msg_path = (By.XPATH, "//span[@class='right padding_t_10 padding_r_10']/a[1]")
    def ERP_OK_Msg(self):
        self.find_element(*self.ERP_OK_Msg_path).click()
        sleep(1)
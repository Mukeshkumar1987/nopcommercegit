
import openpyxl
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pageObject.Login import LoginPage
from utility import XLutils
from utility.Readproperties import Readconfig


class Test_Login_DDT:
    Url = Readconfig.geturl()
    # Email = Readconfig.getEmail()
    # password = Readconfig.getpassword()
    path = "C:\\Users\\mukes\\PycharmProjects\\non commerce\\testcases\\TestData\\login data.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        update_status = []
        for r in range (2,self.rows+1):
            self.Email = XLutils.readData(self.path, 'Sheet1',r,2)
            self.password = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.Enter_Email(self.Email)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login()
            if self.lp.login_Status()==True:
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_loginddt.py-pass.png")
                time.sleep(3)
                self.lp.Click_Menu_Button()
                time.sleep(4)
                self.lp.Click_Logout()
                update_status.append("Pass")
                XLutils.writeData(self.path,'Sheet1',r,4,"pass")
            else:
                update_status.append("Fail")
                XLutils.writeData(self.path,'Sheet1',r, 4,"Fail")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_loginddt.py-fail.png")
        print(update_status)
        if "Fail" in update_status:
            assert True
        else:
            assert False
        self.driver.close()









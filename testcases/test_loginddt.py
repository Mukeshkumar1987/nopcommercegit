
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
        login_status = []
        for r in range (2 , self.rows + 1):
            self.Email = XLutils.readData(self.path, 'Sheet1',r,2)
            self.password = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.Enter_Email(self.Email)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login()
            if self.lp.Title() == "Dashboard / nopCommerce administration":
                time.sleep(2)
                self.lp.Click_Logout()

                login_status.append("Pass")
                XLutils.writeData(self.path,'Sheet1', r, 4, "Pass")
            else:
                login_status.append("Fail")
                # time.sleep(2)
                XLutils.writeData(self.path,'Sheet1', r, 4, "Fail")

        print(login_status)
        if "Fail" not in login_status:
            # time.sleep(5)
            print("login status is passsed")
            # self.log.info("test_login_ddt_006 is Passed")
            assert True
        else:
        # #     # self.log.info("test_login_ddt_006 is Failed")
        # #     print("login status is failed")
            assert False
        self.driver.close()
        # self.log.info("test_login_ddt_006 is Completed")

    #
        # if self.driver.title == "Dashboard / nopCommerce administration":
        #     time.sleep(2)
        #     self.lp.Click_Logout()
        #     assert True
        # else:
        #     assert False
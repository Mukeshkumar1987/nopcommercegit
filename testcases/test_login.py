

import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pageObject.Login import LoginPage
from utility.Logger import LogGenerator
from utility.Readproperties import Readconfig


class Test_Login:
    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()



    def test_login002(self, setup):
        self.driver = setup
        self.log.info("test login 02 is stared")
        self.log.info("opening Browser")
        self.driver.get(self.Url)
        self.log.info("GO to this Url -->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Email-->" + self.Email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("click on login Button")
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_login.py-Pass.png")
            time.sleep(2)
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_login.py-Fail.png")
            assert False







        # if self.lp.Login_status() == True:
        #     self.lp.Click_Menu_Button()
        #     time.sleep(5)
        #     self.lp.Click_Logout()
        #     assert True
        # else:
        #     assert False

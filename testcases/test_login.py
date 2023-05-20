

import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pageObject.Login import LoginPage
from utility.Readproperties import Readconfig


class Test_Login:
    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()



    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.lp.Click_Logout()
            assert True
        else:
            assert False
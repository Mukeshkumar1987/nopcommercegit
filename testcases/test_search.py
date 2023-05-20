import time

from pageObject import Login
from pageObject.AddCustomers import AddCustomer
from pageObject.Login import LoginPage
from pageObject.Search_Emp import Search_Employee
from utility.Readproperties import Readconfig


class Test_Search:
    url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    Password = Readconfig.getpassword()


    def test_search003(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login()
        self.ca = AddCustomer(self.driver)
        self.ca.click_Customers()
        self.ca.click_inside_button()
        self.se = Search_Employee(self.driver)
        self.se.Click_Email("steve_gates@nopCommerce.com")
        self.se.Click_Search()
        # self.se.Click_Search()



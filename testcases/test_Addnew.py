import time
from selenium.webdriver.support import expected_conditions as EC
from pageObject.AddCustomers import AddCustomer
from pageObject.Login import LoginPage
from utility.Readproperties import Readconfig


class Test_Customer:

    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()



    def test_addcust(self,setup):
        self.driver = setup
        self.driver.get(self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.ca = AddCustomer(self.driver)
        self.ca.click_Customers()
        # time.sleep(2)
        self.ca.click_inside_button()
        # time.sleep(2)
        self.ca.Click_AddNew()
        # time.sleep(2)
        self.ca.Enter_Email("dhoni@gmail.com")
        self.ca.Enter_Password("12345679")
        self.ca.Enter_First_Name("Mahaenda")
        self.ca.Enter_Last_Name("singh")
        self.ca.Enter_Gender()
        self.ca.Click_DOB()
        self.ca.Click_Date("12/03/1996")
        self.ca.Click_save()
























# quantityp1 = Select(driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
# quantityp1.select_by_index(2)
#
# quantityp2 = Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
# quantityp2.select_by_index(3)
#
# time.sleep(2)




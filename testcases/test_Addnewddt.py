# import time
# from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

from pageObject.AddCustomers import AddCustomer
from pageObject.Login import LoginPage
from utility import XLutils
from utility.Logger import LogGenerator
from utility.Readproperties import Readconfig

class Test_Customer_DDT:

    Url = Readconfig.geturl()
    Email = Readconfig.getEmail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\mukes\\PycharmProjects\\non commerce\\testcases\\TestData\\emp.xlsx"


    def test_AddCust_ddt003(self,setup):
        self.driver = setup
        self.log.info(" test 003 is staretd")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("GO to this Url-->" + self.Url)
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email(self.Email)
        self.log.info("Enterting the Email" + self.Email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering the Password" + self.password)
        self.lp.Click_Login()
        self.log.info("click the login Button")
        self.ca = AddCustomer(self.driver)
        self.rows = XLutils.getrowCount(self.path,'Sheet1')
        print("Number of rows are -->",self.rows)
        # time.sleep(2)
        self.ca.click_Customers()
        time.sleep(2)
        self.log.info("Click the Customer Buttion")
        # time.sleep(2)
        self.ca.click_inside_button()
        self.log.info("click inside button")
        # time.sleep(2)
        self.ca.Click_AddNew()
        self.log.info("click new add")
        Status_Emp =[]
        for r in range(2,self.rows+1):
            time.sleep(2)
            self.Email = XLutils.readData(self.path, 'Sheet1', r ,2)
            print(self.Email)
            self.password = XLutils.readData(self.path, 'Sheet1',r,3)
            print(self.password)
            self.FirstName = XLutils.readData(self.path, 'Sheet1',r,4)
            print(self.FirstName)
            self.LastName = XLutils.readData(self.path,'Sheet1', r,5)
            print(self.LastName)
            self.Gender = XLutils.readData(self.path, 'Sheet1', r,6)
            print(self.Gender)
            self.DOB = XLutils.readData(self.path, 'Sheet1', r,7)
            print(self.DOB)
            self.ca.Click_save()
            if self.lp.Title() == "Dashboard / nopCommerce administration":
                self.lp.Click_Logout()
                Status_Emp.append("Pass")
                XLutils.writeData(self.path,'Sheet1',r, 8,"Pass")
            else:
                Status_Emp.append("Fail")
                XLutils.writeData(self.path,'Sheet1',r,8,"Fail")

        print(Status_Emp)
        if "Fail" not in Status_Emp:
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
        # self.log.info("click the new Email")
        # self.ca.Enter_Password("rajamohan")
        # self.log.info("Click the new Password")
        # # time.sleep(2)
        # self.ca.Enter_First_name("kaja")
        # self.log.info("click the first name")
        # self.ca.Enter_Last_name("sign")
        # self.log.info("click the last name")
        # self.ca.Enter_Gender()
        # self.log.info("Enter the Gender")
        # self.ca.Click_Date_of_birth("06/20/2000")
        # self.log.info("Enter the DOB")
        # self.ca.Click_Calender()
        # self.log.info("Click the Calender")
        # self.ca.Click_save()
        # # time.sleep(2)
        # self.log.info("click the save")
        # if self.driver.title == "Customers / nopCommerce administration":
        #     self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_Addnew.py-Pass.png")
        #     # time.sleep(2)
        #     self.lp.Click_Logout()
        #     assert True
        # else:
        #     self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\non commerce\\Screenshot\\test_Addnew.py-Fail.png")
        #
        #     assert False


















# quantityp1 = Select(driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]/select[1]"))
# quantityp1.select_by_index(2)
#
# quantityp2 = Select(driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]/select[1]"))
# quantityp2.select_by_index(3)
#
# time.sleep(2)




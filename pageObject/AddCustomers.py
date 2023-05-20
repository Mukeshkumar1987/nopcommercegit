import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from pageObject.Login import LoginPage


from pageObject.Login import LoginPage

class AddCustomer:

    Click_Customers_button_XPATH = (By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    click_Customers_button_XPATH = (By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Click_AddNew_XPATH = (By.XPATH,"//a[@class='btn btn-primary']")
    Text_Email_XPATH = (By.XPATH,"//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='Password']")
    Text_First_Name_XPATH = (By.XPATH,"//input[@id='FirstName']")
    Text_Last_Name_XPATH = (By.XPATH,"//input[@id='LastName']")
    Text_Gender_XPATH = (By.XPATH,"//label[@for='Gender_Male']")
    # Click_DOB_XPATH = (By.XPATH,"//input[@id='DateOfBirth']")
    # Click_Date_XPATH = (By.XPATH,"//span[@class='k-icon k-i-calendar']")
    Click_save_XPATH = (By.XPATH,"//button[@name='save']")

    def  __init__(self,driver):
     self.driver = driver
     self.wait = WebDriverWait(self.driver,10)
#
    def click_Customers(self):
        time.sleep(2)
        self.driver.find_element(*AddCustomer.Click_Customers_button_XPATH).click()
    def click_inside_button(self):
     self.driver.find_element(*AddCustomer.click_Customers_button_XPATH).click()
    def Click_AddNew(self):
     self.driver.find_element(*AddCustomer.Click_AddNew_XPATH).click()
    time.sleep(2)
    def Enter_Email(self,Email):
      self.driver.find_element(*AddCustomer.Text_Email_XPATH).send_keys(Email)

    def Enter_Password(self,Password):
        self.driver.find_element(*AddCustomer.Text_Password_XPATH).send_keys(Password)

    def Enter_First_Name(self,FirstName):
        self.driver.find_element(*AddCustomer.Text_First_Name_XPATH).send_keys(FirstName)
    def Enter_Last_Name(self,LastName):
        self.driver.find_element(*AddCustomer.Text_Last_Name_XPATH).send_keys(LastName)

    def Enter_Gender(self):
        self.driver.find_element(*AddCustomer.Text_Gender_XPATH).click()


    def Click_DOB(self):
        self.driver.find_element(*AddCustomer.Click_DOB_XPATH).click()

    def Click_Date(self,ca):
        self.driver.find_element(*AddCustomer.Click_Date_XPATH).send_keys()
    # def  Click_save(self):
    #     self.driver.find_element(*AddCustomer.Click_save_XPATH).click()
    #     # time.sleep(2)
    #     # self.wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']")))
    #     #
        #
#
# //input[@id='DateOfBirth']
# //a[normalize-space()='18']
# //a[normalize-space()='May 2023']
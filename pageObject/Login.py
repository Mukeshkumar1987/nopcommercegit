import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec, expected_conditions
from selenium.common import NoSuchElementException as Ec


class LoginPage:
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Click_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    CLick_Menu_Button_XPATH = (By.XPATH,"//i[@class='fas fa-cogs']")
    CLick_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 10)

    def Enter_Email(self, email):
        self.driver.find_element(*LoginPage.Text_Email_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def Click_Menu_Button(self):
        # time.sleep(2)
        self.driver.find_element(*LoginPage.CLick_Menu_Button_XPATH).click()

    def Click_Logout(self):
        # time.sleep(2)
        # self.wait.until(Ec.presence_of_element_located((By.XPATH, "//i[@class='fas fa-cogs']")))
        self.driver.find_element(*LoginPage.CLick_Logout_XPATH).click()


    def login_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*LoginPage.CLick_Menu_Button_XPATH)
            return True
        except Ec:
            return False

    # def Title(self):
    #     time.sleep(2)
    #     try:
    #         # wait.until(expected_conditions.visibility_of_element_located(self.CLick_Menu_Button_XPATH))
    #         title = self.driver.title
    #         return title
    #     except:
    #         title = self.driver.title
    #         return title





    #





    # def Login_status(self):
    #     self.driver.implicitly_wait(10)
    #     try:
    #         self.driver.find_element(*LoginPage.CLick_Menu_Button_XPATH)
    #         self.driver.find_element(*LoginPage.CLick_Logout_XPATH)
    #         return True
    #     except Ec:
    #         return False



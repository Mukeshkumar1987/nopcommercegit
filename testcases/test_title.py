from selenium import webdriver


class Test_Page_Title():


    def test_pageTitle(self, setup):
        self.driver = setup
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            assert True
        else:
            assert False
        #self.driver.close()

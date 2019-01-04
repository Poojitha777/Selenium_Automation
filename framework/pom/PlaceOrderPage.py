from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class PlaceOrderPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _coupon = "//input[@id='spc-gcpromoinput']"
    _applybutton = "//input[@value='Apply']"


    def ApplyClick(self):
        self.elementClick(self._applybutton,"xpath")





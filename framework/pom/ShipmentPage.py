from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ShipmentPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _usethisaddress = "//a[contains(text(),'Use this address')]"


    def addressClick(self):
        self.elementClick(self._usethisaddress,"xpath")

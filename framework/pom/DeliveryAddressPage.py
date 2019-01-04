from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class DeliveryAddressPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver





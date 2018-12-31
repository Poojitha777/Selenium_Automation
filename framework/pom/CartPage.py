from framework.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



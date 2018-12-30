from framework.base.Selenium_driver import SeleniumDriver

class ProductPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _product = "(//h2)[1]"

    def productClick(self):
        self.elementClick(self._product,"xpath")




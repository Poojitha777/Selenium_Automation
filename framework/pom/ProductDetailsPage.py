from framework.base.Selenium_driver import SeleniumDriver

class ProductDetailsPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _inStock = "//div[@id='availability']/span"



    def stock(self):
        a = self.getElement(self._inStock,"xpath")
        b = a.text
        return b












from framework.base.Selenium_driver import SeleniumDriver

class ProductDetailsPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _inStock = "//div[@id='availability']/span"

    """method to check if the product is in stock or not"""
    def stock(self):
        a = self.getElement(self._inStock,"xpath")
        b = a.text
        return b












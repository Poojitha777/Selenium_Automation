from framework.base.Selenium_driver import SeleniumDriver

class ProductDetailsPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _inStock = "//div[@id='availability']/span"
    _addCart = "//input[@id='add-to-cart-button']"
    _cartbutton = "//span[@id='nav-cart-count']"

    def stock(self):
        a = self.getElement(self._inStock,"xpath")
        b = a.text
        return b

    def cartClick(self):
        self.elementClick(self._addCart,"xpath")

    def cartCount(self):
        count = self.getElement(self._addCart,"xpath").text
        return count








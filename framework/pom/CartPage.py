from framework.base.Selenium_driver import SeleniumDriver

class CartPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _delete = "//span[@class='a-declarative']/input[1]"
    _subtotal = "//form[@id='gutterCartViewForm']/div[@class='a-box-group sc-buy-box-group']//p/span/span[2]"


    def deleteClick(self):
        self.elementClick(self._delete,"xpath")


    def subtotal(self):
        total = self.getElement(self._subtotal,"xpath").text
        a = total.replace("$","")
        return a


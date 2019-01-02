from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class CartPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    _delete = "//span[@class='a-declarative']/input[1]"
    _subtotal = "//form[@id='gutterCartViewForm']/div[@class='a-box-group sc-buy-box-group']//p/span/span[2]"
    _deleteprice="//form[@id='activeCartViewForm']/div[@class='sc-list-body sc-java-remote-feature']/div[1]/div[4]/div/div[2]/p/span"
    _quantityincrease = "quantity"

    def deleteClick(self):
        self.elementClick(self._delete,"xpath")


    def subtotal(self):
        total = self.getElement(self._subtotal,"xpath").text
        a = total.replace("$","")
        return a

    def quantity(self):
        select = Select(self.getElement(self._quantityincrease, "name"))
        select.select_by_value("2")

    def cart1Price(self):
        var = self.getElement(self._deleteprice,"xpath").text
        var1 = var.replace("$","")
        return var1




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
    _addCart = "//input[@id='add-to-cart-button']"
    _proceedtocheckout = "//a[@id='hlb-ptc-btn-native']"

    def deleteClick(self):
        self.elementClick(self._delete,"xpath")


    def subtotal(self):
        return self.getElement(self._subtotal,"xpath").text.replace("$","")

    def quantity(self):
        select = Select(self.getElement(self._quantityincrease, "name")).select_by_value("2")

    def cart1Price(self):
        return self.getElement(self._deleteprice, "xpath").text.replace("$","")

    """method used to click on ADD TO CART button"""
    def cartClick(self):
        self.elementClick(self._addCart,"xpath")

    def ProceedClick(self):
        self.elementClick(self._proceedtocheckout,"xpath")






from framework.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchbar = "//input[@id='twotabsearchtextbox']"
    _searchbutton = "//input[@type='submit' and @class='nav-input']"
    _addCart = "//input[@id='add-to-cart-button']"
    _cartbutton = "//span[@id='nav-cart-count']"


    def searchBar(self,name):
        self.sendKeys(name, self._searchbar,"xpath")
        self.elementClick(self._searchbutton, "xpath")

    def cartClick(self):
        self.elementClick(self._addCart,"xpath")

    def cartCount(self):
        count = self.getElement(self._cartbutton,"xpath").text
        return int(count)

    def cartButtonClick(self):
        self.elementClick(self._cartbutton, "xpath")





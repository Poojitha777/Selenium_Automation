from framework.base.Selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchbar = "//input[@id='twotabsearchtextbox']"
    _searchbutton = "//input[@type='submit' and @class='nav-input']"


    def searchBar(self,name):
        self.sendKeys(name, self._searchbar,"xpath")
        self.elementClick(self._searchbutton, "xpath")



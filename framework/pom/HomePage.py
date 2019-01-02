from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _searchbar = "//input[@id='twotabsearchtextbox']"
    _searchbutton = "//input[@type='submit' and @class='nav-input']"
    _addCart = "//input[@id='add-to-cart-button']"
    _cartbutton = "//span[@id='nav-cart-count']"
    _department = "//div[@id='nav-shop']/a/span[2]"
    _departmentList = "//div[@id='nav-flyout-shopAll']/div[2]//span"


    """method to enter data on the search bar and click on
    the search icon"""
    def searchBar(self,name):
        self.sendKeys(name, self._searchbar,"xpath")
        self.elementClick(self._searchbutton, "xpath")

    """method used to click on ADD TO CART button"""
    def cartClick(self):
        self.elementClick(self._addCart,"xpath")

    """method used to find the Cart count"""
    def cartCount(self):
        count = self.getElement(self._cartbutton,"xpath").text
        return int(count)

    """method which is used to click on the Cart button"""
    def cartButtonClick(self):
        self.elementClick(self._cartbutton, "xpath")

    """method which is used to hover the mouse on a particular webelement"""
    def mouseHover(self):
        dep = self.getElement(self._department, "xpath")
        actions = ActionChains(self.driver)
        actions.move_to_element(dep).perform()

    """method to return the list of departments"""
    def departmentList(self):
        List = []
        DepLis = self.driver.find_elements_by_xpath(self._departmentList)
        for i in DepLis:
            List.append(i.text)
        return List

    """method which is used to read data from text file"""
    def readFile(self):
        f = open("E:\PROGRAMMINGANGUAGESDOCUMENTS/Department.txt","r")
        return f.readline().replace("\n"," ")









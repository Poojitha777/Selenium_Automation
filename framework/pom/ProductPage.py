from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ProductPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _product = "(//h2)[1]"
    _alexa = "(//h2)[10]"
    _watch = "(//h2)[1]"
    _assertAlexa = "//span[text()='\"Alexa\"']"
    _brand = "//input[@name='s-ref-checkbox-Amazon']"
    _amazon = "//span[text()='Amazon']"
    _review = "//span[text()='4 Stars & Up']"
    _select = "sort"
    _price = "//span[@class='sx-price-whole']"
    _dell = "(//h2)[1]"
    _wait="//div[@id='leftNavContainer']/h3[text()='Show results for']"

    List2 = []

    def productClick(self):
        self.elementClick(self._product,"xpath")

    def alexaClick(self):
        self.elementClick(self._alexa,"xpath")


    def alexa(self):
        txt = self.getElement(self._assertAlexa,"xpath").text
        return txt


    def brandClick(self):
        self.elementClick(self._brand,"xpath")


    def amazonText(self):
        self.waitForElement(self._wait,5,0.5)
        txt1 = self.driver.find_elements_by_xpath(self._amazon)
        # ListAmazon = [a.text for a in txt1]
        ListAmazon = [i.text for i in txt1]
        return ListAmazon

    def reviewClick(self):
        self.elementClick(self._review,"xpath")

    def sort(self):
        selectxpath = self.getElement(self._select,"xpath")
        select = Select(selectxpath)
        select.select_by_visible_text('Price: Low to High')

    def price(self):
       priceList =  self.driver.find_elements_xpath(self._price)
       List1 =[price.text for price in priceList]
       List2 = sorted(List1)
       return List1

    def Dell(self):
        self.elementClick(self._dell,"xpath")

    def watch(self):
        self.elementClick(self._watch,"xpath")





















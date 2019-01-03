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
    _productreview = "//div[@class='s-item-container']/div/div/div[2]/div[3]/div[2]/div[1]/span[1]/span//span"
    _dress = "(//h2)[1]"
    List2 = []

    """method which is used to click on a specific product in the page"""
    def productClick(self):
        self.elementClick(self._product,"xpath")

    """method which is used to click on a specific product in the page """
    def alexaClick(self):
        self.elementClick(self._alexa,"xpath")

    """method which is used to verify the searched text in the search bar"""
    def alexa(self):
        txt = self.getElement(self._assertAlexa,"xpath").text
        return txt

    """method used to filter the brand"""
    def brandClick(self):
        self.elementClick(self._brand,"xpath")

    """method which returns the brand names of all the products for the filtered brand name """
    def amazonText(self):
        self.waitForElement(self._wait,5,0.5)
        txt1 = self.driver.find_elements_by_xpath(self._amazon)
        # ListAmazon = [a.text for a in txt1]
        ListAmazon = [i.text for i in txt1]
        return ListAmazon

    """method which is used to click on the customer review"""
    def reviewClick(self):
        self.elementClick(self._review,"xpath")

    """method which is used to filter 'Price: Low to High' by selecting 
    in the dropdown"""
    def sort(self):
        selectxpath = self.getElement(self._select,"xpath")
        select = Select(selectxpath)
        select.select_by_visible_text('Price: Low to High')

    """method which returns the price of all products in the page"""
    def price(self):
       priceList =  self.driver.find_elements_xpath(self._price)
       List1 =[price.text for price in priceList]
       List2 = sorted(List1)
       return List1

    """method used to click on a particular product"""
    def Dell(self):
        self.elementClick(self._dell,"xpath")

    """method used to click on a particular product"""
    def watch(self):
        self.elementClick(self._watch,"xpath")


    def productReviewClick(self):
        review = self.driver.find_elements_by_xpath(self._productreview)
        ReviewList = []
        for i in review:
            ReviewList.append(i.text[:1])
        return ReviewList

    def dress(self):
        self.elementClick(self._dress,"xpath")
        





















from framework.pom.CartPage import CartPage
from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ReviewFilterValidate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)
        self.cp = CartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_ReviewValidate(self):
        self.pp.readJsonData("D:\Automation\Selenium_Automation\framework\test\ProductName.json","product_name1")
        self.hp.searchBar("Sony")
        self.pp.reviewClick()
        ReviewLL = self.pp.productReviewClick()
        print(ReviewLL)

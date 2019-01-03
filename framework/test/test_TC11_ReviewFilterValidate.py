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
        ReviewEpectedRatings = ['4','4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9','5']
        data = self.hp.readJsonData("D:/Automation/Selenium_Automation/framework/test/ProductName.json","product_name1")
        self.hp.searchBar(data)
        self.pp.reviewClick()
        ReviewLL = self.pp.productReviewClick()
        print(ReviewLL)
        for review in ReviewLL:
            assert review in ReviewEpectedRatings, "Review Filter validation failed"
            print("Review Filter validation successful")


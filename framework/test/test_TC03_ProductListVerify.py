from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ProductPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_searchProduct(self):
        self.hp.searchBar("Alexa")
        productText = self.pp.alexa()
        assert "Alexa" in productText, "Product is not matching"
        print("Product is matching")


    # @pytest.mark.run(order=2)
    # def test_alexaClick(self):
    #     time.sleep(2)
    #     self.pp.alexaClick()
    #     time.sleep(2)

































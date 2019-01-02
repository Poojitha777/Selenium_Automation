from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_RemoveItemValidate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_RemoveProduct(self):
        self.hp.searchBar("dress")
        self.pp.Dell()
        self.hp.cartClick()
        #cart1 = self.hp.cartCount()

        self.hp.searchBar("watch")
        self.pp.watch()
        self.hp.cartClick()
        #cart2 = self.hp.cartCount()
from framework.pom.CartPage import CartPage
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
        self.cp = CartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_RemoveProduct(self):
        self.hp.searchBar("dress")
        self.pp.Dell()
        self.cp.cartClick()
        #cart1 = self.hp.cartCount()
        self.hp.cartButtonClick()
        subtotal1 = self.cp.subtotal()
        print(subtotal1)

        self.hp.searchBar("watch")
        self.pp.watch()
        self.cp.cartClick()
        #cart2 = self.hp.cartCount()
        self.hp.cartButtonClick()
        subtotal2 = self.cp.subtotal()
        print(subtotal2)
        time.sleep(2)
        self.cp.deleteClick()
        time.sleep(2)
        Total = self.cp.subtotal()
        print(Total)
        assert subtotal1 == Total, "Subtotal verified successfully"
        print("Subtotal verification failed ")

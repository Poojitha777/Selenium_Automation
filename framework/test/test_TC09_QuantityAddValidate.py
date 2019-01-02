from framework.pom.CartPage import CartPage
from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_QuantityAddValidate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)
        self.cp = CartPage(self.driver)


    @pytest.mark.run(order=1)
    def test_AddQuantity(self):
        self.hp.searchBar("watch")
        self.pp.watch()
        self.hp.cartClick()
        self.hp.cartButtonClick()
        FirstProductPrice = float(self.cp.cart1Price())
        print(FirstProductPrice)
        Total1 = float(self.cp.subtotal())
        print(Total1)
        cartcount1 = self.hp.cartCount()
        print(cartcount1)
        time.sleep(2)
        self.cp.quantity()
        time.sleep(2)
        Total2 = float(self.cp.subtotal())
        print(Total2)
        subtotal = float(FirstProductPrice*2)
        print(subtotal)
        cartcount=cartcount1+1
        print(cartcount)
        assert Total2 == subtotal, "Quantity failed verification"
        print("Quantity verified successfully")
        







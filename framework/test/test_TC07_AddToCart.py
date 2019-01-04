from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_AddToCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_searchProduct(self):
        self.hp.searchBar("dress")
        self.pp.Dell()
        self.cp.cartClick()
        cart1 = self.hp.cartCount()

        self.hp.searchBar("watch")
        self.pp.watch()
        self.cp.cartClick()
        cart2 = self.hp.cartCount()
        cart = cart1 + 1
        assert cart2==cart, "cart count verified successfully"
        print("cart count failed")






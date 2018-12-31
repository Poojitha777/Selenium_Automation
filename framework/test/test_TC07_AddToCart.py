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
        self.hp.searchBar("dress")
        self.pp.Dell()
        self.pdp.cartClick()
        cart1 = self.pdp.cartCount()
        self.hp.searchBar("watch")
        self.pp.watch()
        self.pdp.cartClick()
        cart2 = self.pdp.cartCount()
        assert cart1==cart2+1, "cart count verified successfully"
        print("cart count failed")






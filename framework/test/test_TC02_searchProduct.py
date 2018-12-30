from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
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
        self.hp.searchBar("iphone")

    @pytest.mark.run(order=2)
    def test_ProductClick(self):
        time.sleep(2)
        self.pp.productClick()
        time.sleep(2)

    @pytest.mark.run(order=3)
    def test_stock(self):
       stock = self.pdp.stock()
       assert "In Stock." in stock, "Product is not in stock"
       print("Product is in stock")


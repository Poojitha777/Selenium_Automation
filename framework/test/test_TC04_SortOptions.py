from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_SortOptions(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=4)
    def test_assertBrand(self):
        self.hp.searchBar("Alexa")
        self.pp.brandClick()
        productText2 = self.pp.amazonText()
        print(productText2)
        for i in productText2:
            assert "Amazon" == i, "brand is not matching"
            print("brand is matching")





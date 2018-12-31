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
        productText2 = self.pp.amazonText()
        for i in productText2:
            assert "Amazon" in i, "Brand is matching"
            print("Brand is not matching")

    @pytest.mark.run(order=3)
    def test_review(self):
        self.pp.reviewClick()

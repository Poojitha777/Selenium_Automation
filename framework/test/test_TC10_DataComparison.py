from framework.pom.CartPage import CartPage
from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_DataComparison(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)
        self.cp = CartPage(self.driver)

    @pytest.mark.run(order=1)
    def test_DataComparison(self):
        self.hp.mouseHover()
        D = self.hp.departmentList()
        print(D)
        for i in range(len(D)):
            time.sleep(1)
            assert self.hp.readFile() in D[i], "Department List matching failed"
            print("Department List matching")





from framework.pom.CartPage import CartPage
from framework.pom.HomePage import HomePage
from framework.pom.ProductPage import ProductPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.pom.SigninPage import SigninPage
from framework.base.Selenium_driver import SeleniumDriver
import pytest
import unittest
import time
import json


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_ReviewFilterValidate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)
        self.cp = CartPage(self.driver)
        self.sg = SigninPage(self.driver)

    @pytest.mark.run(order=1)
    def test_ReviewValidate(self):
        data = self.hp.readJsonData("D:/Automation/Selenium_Automation/framework/test/ProductName.json","product_name2")
        self.hp.searchBar(data)
        self.pp.dress()
        self.cp.cartClick()
        self.cp.ProceedClick()
        un = self.hp.readJsonData("D:/Automation/Selenium_Automation/framework/test/ProductName.json","username")
        self.sg.username(un)
        pw = self.hp.readJsonData("D:/Automation/Selenium_Automation/framework/test/ProductName.json","password")
        self.sg.password(pw)





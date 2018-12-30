from framework.pom.HomePage import HomePage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_HomePage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup2(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)



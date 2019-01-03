from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class SigninPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _username = "//input[@id='ap_email']"
    _password = "//input[@id='ap_password']"
    _signinbutton = "signInSubmit"

    def username(self, username):
        self.sendKeys(username, self._username,"xpath")

    def password(self, password):
        self.sendKeys(password, self._password, "xpath")

    def signinbutton(self):
        self.elementClick(self._signinbutton, "xpath")

    




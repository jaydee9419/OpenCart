import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_login():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("****** test_009_login file started ******")
        self.driver = setup
        self.logger.info("Opening Browser and Application")

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("Filling the credentials")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(ReadConfig.getUsername())
        self.lp.setPassword(ReadConfig.getPassword())
        self.lp.setSubmit()

        self.confmsg = self.lp.getconfirmationmsg()

        self.logger.info("Validating the login status")
        if self.confmsg == "Logged In Successfully":
            assert True
            self.logger.info("Successfully login ito the application")
        else:
            self.logger.error("Failed to login")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "login.png")
            assert False

        self.hp = HomePage(self.driver)
        self.hp.clickLogout()







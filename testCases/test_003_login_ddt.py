import time

from pageObjects.LoginPage import LoginPage
from pageObjects.ExceptionsPage import ExceptionsPage
from pageObjects.HomePage import HomePage

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    path = os.path.abspath(os.curdir)+"\\testdata\\Logindata.xlsx"


    def test_login_ddt(self, setup):
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_ststus = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.ep = ExceptionsPage(self.driver)
        self.hp = HomePage(self.driver)

        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.setSubmit()
            time.sleep(3)

            self.targetpage = self.lp.isLoginpagedisplayed()

            if self.exp == "Valid":
                if self.targetpage == True:
                    lst_ststus.append('Pass')
                    self.hp.clickLogout()
                    time.sleep(3)

                else:
                    lst_ststus.append("Fail")
            elif self.exp == "Invalid":
                if self.targetpage == True:
                    lst_ststus.append("Fail")
                    self.hp.clickLogout()
                    time.sleep(3)
                else:
                    lst_ststus.append("Pass")
        self.driver.close()

        if "Fail" not in lst_ststus:
            assert True
        else:
            assert False










import pytest

from pageObjects.ExceptionsPage import ExceptionsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Test_Exceptions():
    baseURL = "https://practicetestautomation.com/practice-test-exceptions/"

    @pytest.mark.regression
    def test_exceptions(self, setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.ep = ExceptionsPage(self.driver)
        self.ep.clickAddButton()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.ep.btn_save_name))
        )

        self.ep.getSaveButton()




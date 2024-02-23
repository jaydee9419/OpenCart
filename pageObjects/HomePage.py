from selenium.webdriver.common.by import By


class HomePage():
    btn_logout_xpath = "//a[normalize-space()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()


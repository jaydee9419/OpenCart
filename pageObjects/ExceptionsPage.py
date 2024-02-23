from selenium.webdriver.common.by import By


class ExceptionsPage():
    btn_add_id = "add_btn"
    btn_save_name = "Save"

    def __init__(self, driver):
        self.driver = driver

    def clickAddButton(self):
        self.driver.find_element(By.ID, self.btn_add_id).click()

    def getSaveButton(self):
        self.driver.find_element(By.NAME, self.btn_save_name).is_displayed()






from selenium.webdriver.common.by import By

class LoginPage():
    txt_username_name = "username"
    txt_password_name = "password"
    btn_submit_xpath = "//button[@id='submit']"

    txt_confmsg_xpath = "//h1[normalize-space()='Logged In Successfully']"

    btn_logout_xpath = "//a[normalize-space()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, uname):
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(uname)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)

    def setSubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confmsg_xpath).text
        except:
            None

    def isLoginpagedisplayed(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confmsg_xpath).is_displayed()
        except:
            None











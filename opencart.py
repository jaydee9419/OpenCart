from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")

agree_checkbox = driver.find_element(By.NAME, "agree")

# Scroll to the element using JavaScript
driver.execute_script("arguments[0].scrollIntoView(true);", agree_checkbox)

# Add a delay before clicking
time.sleep(2)

# Click the checkbox
agree_checkbox.click()

cont = driver.find_element(By.XPATH, "//button[normalize-space()='Continue']")

cont.click()

time.sleep(5)
driver.close()

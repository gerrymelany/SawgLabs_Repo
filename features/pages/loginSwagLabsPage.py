from selenium.webdriver.common.by import By
import time

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login(self):
        self.driver.get(self.url)

    def enter_username(self, username, tie):
        username_input = self.driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        username_input.send_keys(username)
        time.sleep(tie)

    def enter_password(self, password, tie):
        password_input = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        password_input.send_keys(password)
        time.sleep(tie)

    def click_login_button(self, tie):
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(tie)
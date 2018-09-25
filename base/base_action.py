from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll_frequency=1.0):
        feature_by, feature_value = feature
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(lambda x: x.find_element(feature_by, feature_value))

    def find_elements(self, feature, timeout=10, poll_frequency=1.0):
        feature_by, feature_value = feature
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        return wait.until(lambda x: x.find_elements(feature_by, feature_value))

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def toast1(self, message, timeout=3, poll_frequency=0.1):
        message = By.XPATH, "//*[contains(@text,'" + message + "')]"
        try:

            if self.find_element(message, timeout, poll_frequency).text:
                return True

        except Exception:
            return False

    def toast2(self, login_button):
        try:
            if self.find_element(login_button).get_attribute('enabled') == "ture":
                return True
        except Exception:
            return False

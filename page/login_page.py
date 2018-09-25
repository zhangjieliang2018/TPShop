from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    phone_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_phone(self, phone):
        self.input(self.phone_text, phone)

    def input_password(self, password):
        self.input(self.password_text, password)

    def click_login(self):
        self.click(self.login_button)

    def assert_login1(self, toast_text):
        assert self.toast1(toast_text)

    def assert_login2(self):
        assert not self.toast2(self.login_button)

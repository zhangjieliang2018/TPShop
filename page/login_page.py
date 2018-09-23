from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    phone_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    toast_text = "登录成功"

    def input_phone(self):
        self.input(self.phone_text, "18503080305")

    def input_passwd(self):
        self.input(self.password_text, "123456")

    def click_login(self):
        self.click(self.login_button)

    def assert_login(self):
         assert self.toast(self.toast_text)

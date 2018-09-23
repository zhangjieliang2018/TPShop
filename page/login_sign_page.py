from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginSignPage(BaseAction):

    login_sign_button = By.XPATH , "//*[@text = '登录/注册']"

    def click_login_sign(self):
        self.click(self.login_sign_button)
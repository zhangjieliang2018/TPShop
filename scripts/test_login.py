from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.mine.click_mine()
        self.page.login_sign.click_login_sign()
        self.page.login.input_phone()
        self.page.login.input_passwd()
        self.page.login.click_login()
        self.page.login.assert_login()

    def teardown(self):
        self.driver.quit()

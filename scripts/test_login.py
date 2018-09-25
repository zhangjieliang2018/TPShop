import pytest

from base.analyze_data import data_analyze
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", data_analyze('login1'))
    def test_login_1(self, args):
        self.page.mine.click_mine()
        self.page.login_sign.click_login_sign()
        self.page.login.input_phone(args["phone"])
        self.page.login.input_password(args["password"])
        self.page.login.click_login()
        self.page.login.assert_login1(args["toast_text"])

    @pytest.mark.parametrize("args", data_analyze('login2'))
    def test_login_2(self, args):
        self.page.mine.click_mine()
        self.page.login_sign.click_login_sign()
        self.page.login.input_phone(args["phone"])
        self.page.login.input_password(args["password"])
        self.page.login.assert_login2()
    def teardown(self):
        self.driver.quit()

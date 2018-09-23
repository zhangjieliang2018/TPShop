from page.login_page import LoginPage
from page.login_sign_page import LoginSignPage
from page.mine_page import MinePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login_sign(self):
        return LoginSignPage(self.driver)
    @property
    def login(self):
        return LoginPage(self.driver)

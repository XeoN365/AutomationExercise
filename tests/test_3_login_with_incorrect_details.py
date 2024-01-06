from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage
from utils import utils


def test_case(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    random_email = f"{utils.random_string()}@{utils.random_string(4)}.com"
    random_password = utils.random_string(10)
    login_page.login_enter_email(random_email)
    login_page.login_enter_password(random_password)
    login_page.click_login()

    login_page.check_incorrect_login_label()

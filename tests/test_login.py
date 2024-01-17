from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage
from utils import utils


def test_login_with_correct_details(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.login_user(user_data["email"], user_data["password"])
    homepage.check_login_status(user_data["first_name"], user_data["last_name"])


def test_login_with_incorrect_details(init_driver):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    random_email = utils.random_email()
    random_password = utils.random_string(10)
    login_page.login_user(random_email, random_password)

    login_page.check_incorrect_login_label()

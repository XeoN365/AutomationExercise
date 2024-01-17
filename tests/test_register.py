from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage
from ae_website.AEAccountAction import AccountActionPage
from ae_website.AESignUp import SignUpPage


def test_register(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)
    signup_page = SignUpPage(init_driver)
    account_actions_page = AccountActionPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.signup_user(user_data["first_name"], user_data["email"])

    signup_page.register_user(user_data)

    account_actions_page.verify_account_created()

    homepage.check_login_status(user_data["first_name"], user_data["last_name"])


def test_register_with_existing_email(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.signup_user(user_data["first_name"], user_data["email"])
    login_page.check_incorrect_signup_label()

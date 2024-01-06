from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage


def test_case(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.signup_enter_name(user_data["first_name"])
    login_page.signup_enter_email(user_data["email"])
    login_page.click_signup()

    login_page.check_incorrect_signup_label()

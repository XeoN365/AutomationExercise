from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage


def test_case(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.login_enter_email(user_data["email"])
    login_page.login_enter_password(user_data["password"])
    login_page.click_login()

    homepage.check_login_status(f"{user_data['first_name']} {user_data['last_name']}")
    homepage.logout()

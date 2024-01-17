from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage
from ae_website.AEAccountAction import AccountActionPage


def test_remove(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)
    account_actions_page = AccountActionPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.login_user(user_data["email"], user_data["password"])

    homepage.check_login_status(user_data["first_name"], user_data["last_name"])
    homepage.delete_account()

    account_actions_page.verify_account_deleted()

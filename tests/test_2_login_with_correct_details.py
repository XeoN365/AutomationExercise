from ae_website.AEHomePage import HomePage
from ae_website.AELoginPage import LoginPage
from ae_website.AEAccountAction import AccountActionPage
from ae_website.AESignUp import SignUpPage


def test_case(init_driver, user_data):
    homepage = HomePage(init_driver)
    login_page = LoginPage(init_driver)
    signup_page = SignUpPage(init_driver)
    account_actions_page = AccountActionPage(init_driver)

    homepage.go_to_website()
    homepage.check_website_visible()
    homepage.login()

    login_page.check_new_user_label()
    login_page.signup_enter_name(user_data["first_name"])
    login_page.signup_enter_email(user_data["email"])
    login_page.click_signup()

    signup_page.select_title(user_data["title"])
    signup_page.enter_name(f"{user_data['first_name']} {user_data['last_name']}")
    signup_page.enter_password(user_data["password"])
    signup_page.select_dob(
        user_data["dob"][0], user_data["dob"][1], user_data["dob"][2]
    )
    signup_page.check_newsletter()
    signup_page.check_special_offers()
    signup_page.enter_first_name(user_data["first_name"])
    signup_page.enter_last_name(user_data["last_name"])
    signup_page.enter_address(user_data["address"])
    signup_page.select_country(user_data["country"])
    signup_page.enter_state(user_data["state"])
    signup_page.enter_city(user_data["city"])
    signup_page.enter_zipcode(user_data["zipcode"])
    signup_page.enter_mobile_number(user_data["mobile_number"])
    signup_page.register()

    account_actions_page.verify_account_created()
    account_actions_page.click_continue()

    homepage.logout()

    login_page.login_enter_email(user_data["email"])
    login_page.login_enter_password(user_data["password"])
    login_page.click_login()

    homepage.check_login_status(f"{user_data['first_name']} {user_data['last_name']}")

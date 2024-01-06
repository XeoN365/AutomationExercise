from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "new_user_label": ("XPATH", '//div[@class="signup-form"]/h2'),
        "login_label": ("XPATH", '//div[@class="login-form"]/h2'),
        "signup_name_textbox": ("XPATH", '//input[@data-qa="signup-name"]'),
        "signup_email_textbox": ("XPATH", '//input[@data-qa="signup-email"]'),
        "signup_button": ("XPATH", '//button[@data-qa="signup-button"]'),
        "login_email_textbox": ("XPATH", '//input[@data-qa="login-email"]'),
        "login_password_textbox": ("XPATH", '//input[@data-qa="login-password"]'),
        "login_button": ("XPATH", '//button[@data-qa="login-button"]'),
        "incorrect_login_label": ("XPATH", '//form[@action="/login"]/p'),
        "incorrect_signup_label": ("XPATH", '//form[@action="/signup"]/p'),
    }

    def check_new_user_label(self):
        assert self.new_user_label.get_text() == "New User Signup!"

    def check_login_label(self):
        assert self.login_label.get_text() == "Login to your account"

    def signup_enter_name(self, name):
        self.signup_name_textbox.set_text(name)

    def signup_enter_email(self, email):
        self.signup_email_textbox.set_text(email)

    def click_signup(self):
        self.signup_button.click_button()

    def login_enter_email(self, email):
        self.login_email_textbox.set_text(email)

    def login_enter_password(self, password):
        self.login_password_textbox.set_text(password)

    def click_login(self):
        self.login_button.click_button()

    def check_incorrect_login_label(self):
        assert (
            self.incorrect_login_label.get_text()
            == "Your email or password is incorrect!"
        )

    def check_incorrect_signup_label(self):
        assert self.incorrect_signup_label.get_text() == "Email Address already exist!"

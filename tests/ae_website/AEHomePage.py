from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "home_button": ("XPATH", '//div[@class="logo pull-left"]/a/img'),
        "login_button": ("XPATH", '//a[@href="/login"]'),
        "login_status": ("XPATH", '//ul[@class="nav navbar-nav"]/li[last()]/a'),
        "delete_account_button": ("XPATH", '//a[@href="/delete_account"]'),
        "logout_button": ("XPATH", '//a[@href="/logout"]'),
    }

    def check_website_visible(self):
        assert self.home_button.visibility_of_element_located() != None

    def login(self):
        self.login_button.click_button()

    def check_login_status(self, first_name, last_name):
        assert (
            self.login_status.get_text() == f"Logged in as {first_name} {last_name}"
        ), "'Logged in as' label is not displayed!"

    def delete_account(self):
        self.delete_account_button.click_button()

    def go_to_website(self):
        self.driver.get("http://automationexercise.com")

    def logout(self):
        self.logout_button.click_button()

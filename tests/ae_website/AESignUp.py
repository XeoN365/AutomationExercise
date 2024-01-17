from seleniumpagefactory.Pagefactory import PageFactory


class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "title_radio": ("XPATH", '//input[@value="Mr"]'),
        "name_textbox": ("XPATH", '//input[@data-qa="name"]'),
        "password_textbox": ("XPATH", '//input[@data-qa="password"]'),
        "days_dropdown": ("XPATH", '//select[@data-qa="days"]'),
        "months_dropdown": ("XPATH", '//select[@data-qa="months"]'),
        "years_dropdown": ("XPATH", '//select[@data-qa="years"]'),
        "newsletter_checkbox": ("XPATH", '//input[@name="newsletter"]'),
        "special_offers_checkbox": ("XPATH", '//input[@name="optin"]'),
        "first_name_textbox": ("XPATH", '//input[@data-qa="first_name"]'),
        "last_name_textbox": ("XPATH", '//input[@data-qa="last_name"]'),
        "address_textbox": ("XPATH", '//input[@data-qa="address"]'),
        "country_dropdown": ("XPATH", '//select[@data-qa="country"]'),
        "state_textbox": ("XPATH", '//input[@data-qa="state"]'),
        "city_textbox": ("XPATH", '//input[@data-qa="city"]'),
        "zipcode_textbox": ("XPATH", '//input[@data-qa="zipcode"]'),
        "mobile_number_textbox": ("XPATH", '//input[@data-qa="mobile_number"]'),
        "register_button": ("XPATH", '//button[@data-qa="create-account"]'),
    }

    def select_title(self, title):
        self.title_radio.click_button()

    def enter_name(self, name):
        self.name_textbox.clear_text()
        self.name_textbox.set_text(name)

    def enter_password(self, password):
        self.password_textbox.set_text(password)

    def select_dob(self, day, month, year):
        self.days_dropdown.select_element_by_value(str(day))
        self.months_dropdown.select_element_by_value(str(month))
        self.years_dropdown.select_element_by_value(str(year))

    def check_newsletter(self):
        self.newsletter_checkbox.click_button()

    def check_special_offers(self):
        self.special_offers_checkbox.click_button()

    def enter_first_name(self, first_name):
        self.first_name_textbox.set_text(first_name)

    def enter_last_name(self, last_name):
        self.last_name_textbox.set_text(last_name)

    def enter_address(self, address):
        self.address_textbox.set_text(address)

    def select_country(self, country):
        self.country_dropdown.select_element_by_value(country)

    def enter_state(self, state):
        self.state_textbox.set_text(state)

    def enter_city(self, city):
        self.city_textbox.set_text(city)

    def enter_zipcode(self, zipcode):
        self.zipcode_textbox.set_text(zipcode)

    def enter_mobile_number(self, mobile_number):
        self.mobile_number_textbox.set_text(mobile_number)

    def register(self):
        self.register_button.click_button()

    def register_user(self, user_data):
        self.select_title(user_data["title"])
        self.enter_name(f"{user_data['first_name']} {user_data['last_name']}")
        self.enter_password(user_data["password"])
        self.select_dob(user_data["dob"][0], user_data["dob"][1], user_data["dob"][2])
        self.check_newsletter()
        self.check_special_offers()
        self.enter_first_name(user_data["first_name"])
        self.enter_last_name(user_data["last_name"])
        self.enter_address(user_data["address"])
        self.select_country(user_data["country"])
        self.enter_state(user_data["state"])
        self.enter_city(user_data["city"])
        self.enter_zipcode(user_data["zipcode"])
        self.enter_mobile_number(user_data["mobile_number"])
        self.register()

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import string
import random


def element_present(driver, by, element_code):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, element_code))
        )
        element_present = True
    except Exception as e:
        element_present = False
    return element_present


def random_string(string_length=1):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    alphabet = alphabet_lower + alphabet_upper
    if string_length == 1:
        string_length = random.randint(3, 10)
    return random.sample(alphabet, string_length)


def register_first(driver, user_data):
    # Click login button
    login_button = driver.find_element(By.XPATH, '//a[@href="/login"]')
    login_button.click()

    # Identify that registration form is present
    new_user_text_present = element_present(
        driver,
        By.XPATH,
        '//div[@class="signup-form"]/h2[contains(text(), "New User Signup!")]',
    )
    assert new_user_text_present == True

    # find name textbox and type person's name
    name_textbox = driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]')
    name_textbox.send_keys(user_data["first_name"])

    # find email textbox and type person's email address
    email_textbox = driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
    email_textbox.send_keys(user_data["email"])

    # find sign up button and click it
    sign_up_button = driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]')
    sign_up_button.click()

    ###Registration form
    # find title radio buttons and click appropriate one
    title_radio = driver.find_element(
        By.XPATH, f'//input[@value="{user_data["title"]}"]'
    )
    title_radio.click()

    # find name textbox and fill it with person's name
    name2_textbox = driver.find_element(By.XPATH, '//input[@data-qa="name"]')
    # clear it first before filling it
    name2_textbox.clear()
    name2_textbox.send_keys(f"{user_data['first_name']} {user_data['last_name']}")

    # find password textbox and fill it with person's password
    password_textbox = driver.find_element(By.XPATH, '//input[@data-qa="password"]')
    password_textbox.send_keys(user_data["password"])

    # find 'Date of birth" dropdown boxes and select correct dob
    dob_days_dropdown = driver.find_element(By.XPATH, f'//select[@data-qa="days"]')
    days_options = Select(dob_days_dropdown)
    days_options.select_by_value(str(user_data["dob"][0]))

    dob_months_dropdown = driver.find_element(By.XPATH, f'//select[@data-qa="months"]')
    months_options = Select(dob_months_dropdown)
    months_options.select_by_value(str(user_data["dob"][1]))

    dob_years_dropdown = driver.find_element(By.XPATH, f'//select[@data-qa="years"]')
    years_options = Select(dob_years_dropdown)
    years_options.select_by_value(str(user_data["dob"][2]))

    # Sign up for newsletter and receive special offers
    newsletter_checkbox = driver.find_element(By.XPATH, '//input[@name="newsletter"]')
    newsletter_checkbox.click()

    special_offers_checkbox = driver.find_element(By.XPATH, '//input[@name="optin"]')
    special_offers_checkbox.click()

    # Fill out personal information
    first_name_textbox = driver.find_element(By.XPATH, '//input[@data-qa="first_name"]')
    first_name_textbox.send_keys(user_data["first_name"])

    last_name_textbox = driver.find_element(By.XPATH, '//input[@data-qa="last_name"]')
    last_name_textbox.send_keys(user_data["last_name"])

    address_textbox = driver.find_element(By.XPATH, '//input[@data-qa="address"]')
    address_textbox.send_keys(user_data["address"])

    country_dropdown = driver.find_element(By.XPATH, '//select[@data-qa="country"]')
    country_options = Select(country_dropdown)
    country_options.select_by_value(user_data["country"])

    state_textbox = driver.find_element(By.XPATH, '//input[@data-qa="state"]')
    state_textbox.send_keys(user_data["state"])

    city_textbox = driver.find_element(By.XPATH, '//input[@data-qa="city"]')
    city_textbox.send_keys(user_data["city"])

    zipcode_textbox = driver.find_element(By.XPATH, '//input[@data-qa="zipcode"]')
    zipcode_textbox.send_keys(user_data["postcode"])

    mobile_number_textbox = driver.find_element(
        By.XPATH, '//input[@data-qa="mobile_number"]'
    )
    mobile_number_textbox.send_keys(user_data["phone"])

    register_button = driver.find_element(
        By.XPATH, '//button[@data-qa="create-account"]'
    )
    register_button.click()

    # Verify that registration form is complete
    account_created_text_present = element_present(
        driver,
        By.XPATH,
        '//h2[@data-qa="account-created"]/b[contains(text(), "Account Created!")]',
    )
    assert account_created_text_present == True

    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.click()

    logout_button = driver.find_element(By.XPATH, '//a[@href="/logout"]')
    logout_button.click()


def test_case(init_driver, user_data):
    driver = init_driver
    driver.get("http://automationexercise.com")

    register_first(driver, user_data)

    login_text_present = element_present(
        driver,
        By.XPATH,
        '//div[@class="login-form"]/h2[contains(text(), "Login to your account")]',
    )
    assert login_text_present == True

    # find name textbox and type person's name
    name_textbox = driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
    name_textbox.send_keys(user_data["email"])

    # find email textbox and type person's email address
    email_textbox = driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
    email_textbox.send_keys(user_data["password"])

    # find login button and click it
    login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
    login_button.click()

    logged_in_status = driver.find_element(
        By.XPATH, '//ul[@class="nav navbar-nav"]/li[last()]/a'
    )
    assert (
        logged_in_status.text
        == "Logged in as " + user_data["first_name"] + " " + user_data["last_name"]
    )

    # Delete account
    delete_account_button = driver.find_element(
        By.XPATH, '//a[@href="/delete_account"]'
    )
    delete_account_button.click()

    account_deleted_text_present = element_present(
        driver,
        By.XPATH,
        '//h2[@data-qa="account-deleted"]/b[contains(text(), "Account Deleted!")]',
    )
    assert account_deleted_text_present == True

    # Press continue button
    continue_button = driver.find_element(By.XPATH, '//a[@data-qa="continue-button"]')
    continue_button.click()

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


# Gemerate random string with x length of characters
def random_string(string_length=1):
    alphabet_lower = list(string.ascii_lowercase)
    alphabet_upper = list(string.ascii_uppercase)
    alphabet = alphabet_lower + alphabet_upper
    if string_length == 1:
        string_length = random.randint(3, 10)
    return "".join(random.sample(alphabet, string_length))


def test_case(init_driver, user_data):
    driver = init_driver
    driver.get("http://automationexercise.com")

    # Go to login page
    login_button = driver.find_element(By.XPATH, '//a[@href="/login"]')
    login_button.click()

    # verify that login form is present
    login_text_present = element_present(
        driver,
        By.XPATH,
        '//div[@class="login-form"]/h2[contains(text(), "Login to your account")]',
    )
    assert login_text_present == True

    # find name textbox and type random email
    name_textbox = driver.find_element(By.XPATH, '//input[@data-qa="login-email"]')
    name_textbox.send_keys(f"{random_string()}@{random_string()}.com")

    # find email textbox and type random password
    email_textbox = driver.find_element(By.XPATH, '//input[@data-qa="login-password"]')
    email_textbox.send_keys(random_string(10))

    # find login button and click it
    login_button = driver.find_element(By.XPATH, '//button[@data-qa="login-button"]')
    login_button.click()

    # verify that error message is present
    incorrect_details_text = driver.find_element(By.XPATH, '//form[@action="/login"]/p')
    assert incorrect_details_text.text == "Your email or password is incorrect!"

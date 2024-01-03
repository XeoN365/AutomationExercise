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


def test_case(init_driver, user_data):
    driver = init_driver
    driver.get("http://automationexercise.com")

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

    email_in_use_text = driver.find_element(By.XPATH, '//form[@action="/signup"]/p')
    assert email_in_use_text.text == "Email Address already exist!"

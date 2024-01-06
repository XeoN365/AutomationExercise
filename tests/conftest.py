import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture
def user_data():
    """Definition of user data for test
    Returns: dictionary containing:
    - title: string
    - first_name: string
    - last_name: string
    - gender: string
    - email: string
    - phone: string
    - username: string
    - password: string
    - dob: tuple(day,month,year) as ints
    - address: string
    - city: string
    - country: string
    - state: string
    - postcode: string
    """
    person = dict()
    person["title"] = "Mr"
    person["first_name"] = "George"
    person["last_name"] = "Kutanga"
    person["gender"] = "Male"
    person["email"] = "george.kutanga@testing.com"
    person["mobile_number"] = "+447758875436"
    person["username"] = "george.kutanga"
    person["password"] = "randompassword"
    person["dob"] = (21, 12, 1990)
    person["address"] = "123 Main Street"
    person["city"] = "Los Angelios"
    person["country"] = "United States"
    person["state"] = "CA"
    person["zipcode"] = "TE5 1AA"
    return person


@pytest.fixture
def init_driver():
    """Initiate driver for test"""
    chrome_options = Options()
    chrome_options.add_argument(
        f"--load-extension={os.getcwd()}/tests/extensions/cfhdojbkjhnklbpkdaibdccddilifddb/3.21.1_0/"
    )
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    # wait for adblock page to be loaded and close it
    wait = WebDriverWait(driver, 10)
    wait.until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[0])

    yield driver
    driver.quit()

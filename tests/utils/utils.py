from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    return "".join(random.sample(alphabet, string_length))


def random_email():
    return random_string() + "@" + random_string() + ".com"

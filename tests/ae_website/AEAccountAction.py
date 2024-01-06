from seleniumpagefactory.Pagefactory import PageFactory


class AccountActionPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "account_created_label": ("XPATH", '//h2[@data-qa="account-created"]/b'),
        "account_deleted_label": ("XPATH", '//h2[@data-qa="account-deleted"]/b'),
        "continue_button": ("XPATH", '//a[@data-qa="continue-button"]'),
    }

    def verify_account_created(self):
        label = self.account_created_label.get_text()
        assert label == "ACCOUNT CREATED!"

    def verify_account_deleted(self):
        label = self.account_deleted_label.get_text()
        assert label == "ACCOUNT DELETED!"

    def click_continue(self):
        self.continue_button.click_button()

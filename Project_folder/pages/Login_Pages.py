import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


class LoginPage(Commons):

    PHONE_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    REMEMBER_ME = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/span/span/i')
    SUBMIT_BUTTON = (U.By.CLASS_NAME, 'form_submitBtn')
    GOOGLE_LOGIN = (U.By.CLASS_NAME, 'login_google')
    FACEBOOK_LOGIN = (U.By.CLASS_NAME, 'login_facebook')
    TWITTER_LOGIN = (U.By.CLASS_NAME, 'login_twitter')

    def insert_phone_number(self, phone_number):
        self.wait_for(LoginPage.PHONE_NUMBER)
        self.insert(LoginPage.PHONE_NUMBER, phone_number)

    def click_remember_me(self):
        self.wait_for_clickable(LoginPage.REMEMBER_ME).click()

    def click_submit_button(self):
        self.wait_for_clickable(LoginPage.SUBMIT_BUTTON).click()

    def click_google_login(self):
        self.wait_for_clickable(LoginPage.GOOGLE_LOGIN).click()

    def click_facebook_login(self):
        self.wait_for_clickable(LoginPage.FACEBOOK_LOGIN).click()

    def click_twitter_login(self):
        self.wait_for_clickable(LoginPage.TWITTER_LOGIN).click()

    def log_in_remember_me(self, phone_number):
        Commons.click_login_signup(self)
        Commons.click_login_signup(self)
        LoginPage.insert_phone_number(self, phone_number)
        LoginPage.click_remember_me(self)
        LoginPage.click_submit_button(self)

    def log_in_no_remember(self, phone_number):
        Commons.click_login_signup(self)
        LoginPage.insert_phone_number(self, phone_number)
        LoginPage.click_submit_button(self)

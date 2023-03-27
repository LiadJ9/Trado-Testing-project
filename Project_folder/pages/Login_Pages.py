import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


class LoginPage(Commons):

    # Login Locators

    PHONE_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    REMEMBER_ME = (U.By.CSS_SELECTOR, '.micon-check')
    SUBMIT_BUTTON = (U.By.CLASS_NAME, 'form_submitBtn')
    GOOGLE_LOGIN = (U.By.CLASS_NAME, 'login_google')
    FACEBOOK_LOGIN = (U.By.CLASS_NAME, 'login_facebook')
    TWITTER_LOGIN = (U.By.CLASS_NAME, 'login_twitter')
    LOGIN_ERROR = (U.By.CSS_SELECTOR, '.form_message')
    GOOGLE_AUTH_LINK = 'https://accounts.google.com/signin/oauth/success'

    def insert_phone_number(self, phone_number):
        self.wait_for(LoginPage.PHONE_NUMBER)
        self.insert(LoginPage.PHONE_NUMBER, phone_number)

    def assert_remember_me_worked(self):
        self.wait_for(LoginPage.PHONE_NUMBER)
        txt = self.get_text(LoginPage.PHONE_NUMBER)
        return txt

    def click_remember_me(self):
        self.wait_for(LoginPage.REMEMBER_ME).click()

    def click_submit_button(self):
        self.wait_for(LoginPage.SUBMIT_BUTTON).click()

    def click_google_login(self):
        self.wait_for(LoginPage.GOOGLE_LOGIN).click()

    def click_facebook_login(self):
        self.wait_for(LoginPage.FACEBOOK_LOGIN).click()

    def click_twitter_login(self):
        self.wait_for(LoginPage.TWITTER_LOGIN).click()

    def log_in(self, phone_number, remember_me, security_off):
        Commons.click_login_signup(self)
        LoginPage.insert_phone_number(self, phone_number)
        if remember_me:
            LoginPage.click_remember_me(self)
        LoginPage.click_submit_button(self)
        Commons.insert_security_code(self, phone_number, security_off)
        U.sleep(1)

    def find_error(self):
        self.wait_for(LoginPage.LOGIN_ERROR)
        error = self.get_text(LoginPage.LOGIN_ERROR)
        return error

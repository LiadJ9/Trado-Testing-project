from Project_folder.pages.common_page import Commons
import Project_folder.pages.Utils.TRADO_UTILS as U
import Project_folder.MongoDB_requests as R


class SignupPage(Commons):
    SIGNUP_SELECT = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/span[2]')
    PHONE_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    COMPANY = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input')
    CONFIRM_PRIVACY_POLICY = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/span/span/i')
    MAIL_ADS = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[4]/span/span/span/i')
    SUBMIT_BUTTON = (U.By.CLASS_NAME, 'form_submitBtn')
    GOOGLE_LOGIN = (U.By.CLASS_NAME, 'login_google')
    FACEBOOK_LOGIN = (U.By.CLASS_NAME, 'login_facebook')
    TWITTER_LOGIN = (U.By.CLASS_NAME, 'login_twitter')
    FIRST_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    SECOND_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input')
    THIRD_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/input')
    FOURTH_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[4]/span/input')
    FIFTH_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[5]/span/input')
    SUBMIT_CONFIRMATION = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/input')
    RESTAURANTS = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div[1]')
    COCKTAILS = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[2]/div[2]')
    CONFIRM_PREFERENCE = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/div/div[3]/button')

    # Basic setup pages #

    def select_signup(self):
        self.wait_for_clickable(SignupPage.SIGNUP_SELECT).click()

    def insert_phone_number(self, phone_number):
        self.wait_for(SignupPage.PHONE_NUMBER)
        self.insert(SignupPage.PHONE_NUMBER, phone_number)

    def insert_company(self, number):
        self.wait_for(SignupPage.COMPANY)
        self.insert(SignupPage.COMPANY, U.keys.CLEAR)
        self.insert(SignupPage.COMPANY, number)

    # CONFIRMS PRIVACY POLICY

    def confirm_privacy_policy(self):
        self.wait_for(SignupPage.CONFIRM_PRIVACY_POLICY).click()

    # ADS ENABLED BY DEFAULT - THIS DISABLES THEM IF NEEDED

    def click_main_ads_button(self):
        self.wait_for(SignupPage.MAIL_ADS).click()

    # SUBMITS INITIAL ACCOUNT CREATION REQUEST

    def click_submit(self):
        self.wait_for_clickable(SignupPage.SUBMIT_BUTTON).click()

    # SELECTS PREFERENCE

    def click_restaurant(self):
        self.wait_for_clickable(SignupPage.RESTAURANTS).click()

    def click_cocktails(self):
        self.wait_for_clickable(SignupPage.COCKTAILS).click()

    def confirm_preference(self):
        self.wait_for_clickable(SignupPage.CONFIRM_PREFERENCE).click()

    # USED TO SUBMIT THE SECURITY CONFIRMATION CODE :)

    def click_submit_confirmation(self):
        self.wait_for_clickable(SignupPage.SUBMIT_CONFIRMATION).click()

    # TO BE USED ONLY IN THE SECURITY CODE PAGE - INSERTS THE SECURITY CODE STRAIGHT FROM THE DB - IT ALSO RETURNS IT FOR LATER USE (MAYBE)

    def insert_security_code(self, phone_number, false_flag):
        self.wait_for(SignupPage.SUBMIT_CONFIRMATION)
        requests = R.MongoRequests()
        login_code = requests.find_login_code(phone_number)
        signup_list = [
            SignupPage.FIRST_NUMBER,
            SignupPage.SECOND_NUMBER,
            SignupPage.THIRD_NUMBER,
            SignupPage.FOURTH_NUMBER,
            SignupPage.FIFTH_NUMBER
        ]
        list_count = 0
        if false_flag:
            for f in '00000':
                self.insert(signup_list[list_count], f)
                list_count += 1
        else:
            for i in login_code:
                self.insert(signup_list[list_count], i)
                list_count += 1
        SignupPage.click_submit_confirmation(self)
        return login_code

    # Advanced pages #

    # all additional variables are used to determine which actions should be performed for additional testing parameters :0 (wow!)
    # FOR A CHOICE TO BE "ACTIVE" RETURN TRUE VARIABLE
    # pref1 = Restaurants  # pref2 = Cocktails
    # validcode = Security code validity || # valid_phone = Phone num validity || # valid_company
    # Privacy = Privacy checked
    # ads = Ads checked

    def sign_up(self, pref1, pref2, validcode, valid_company, privacy, valid_phone, ads):
        Commons.click_login_signup(self)
        SignupPage.select_signup(self)
        if valid_phone:
            phone_number = Commons.random_phone_number()
        else:
            phone_number = 'blargabcdk'
        if valid_company:
            company_num = 7
        else:
            company_num = 'g'
        SignupPage.insert_phone_number(self, phone_number)
        SignupPage.insert_company(self, company_num)
        if privacy:
            SignupPage.confirm_privacy_policy(self)
        if not ads:
            SignupPage.click_main_ads_button(self)
        SignupPage.click_submit(self)
        if validcode:
            login_code = SignupPage.insert_security_code(self, phone_number, False)
        else:
            login_code = SignupPage.insert_security_code(self, phone_number, True)
        if pref1:
            SignupPage.click_restaurant(self)
        if pref2:
            SignupPage.click_cocktails(self)
        SignupPage.confirm_preference(self)
        self.wait_for_invisibility(SignupPage.CONFIRM_PREFERENCE)
        return phone_number, login_code

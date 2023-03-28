from Project_folder.pages.Utils import TRADO_UTILS as U
import Project_folder.MongoDB_requests as R


class Commons(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = U.wdw(self.driver, 10)
        self._qwait = U.wdw(self.driver, 2)

    def wait_for(self, locator):
        return self._wait.until(U.ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(U.ec.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        return self._wait.until(U.ec.invisibility_of_element(locator))

    def quick_wait_for_invisibility(self, locator):
        return self._qwait.until(U.ec.invisibility_of_element(locator))

    def wait_for_window_number_to_change(self, num):
        return self._wait.until(U.ec.number_of_windows_to_be(num))

    def switch_tabs(self, tab_to_switch):
        self.wait_for_window_number_to_change(2)
        for tab in self.driver.window_handles:
            if tab != tab_to_switch:
                self.driver.switch_to.window(tab)
                break

    def wait_for_url_change(self, url):
        return self._wait.until(U.ec.url_to_be(url))

    def wait_for_alert(self):
        return self._wait.until(U.ec.alert_is_present())

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_many(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        temp = self.driver.find_element(*locator)
        return temp.text

    def insert(self, locator, insertion):
        locator = self.driver.find_element(*locator)
        locator.send_keys(insertion)

    def clear(self, locator):
        locator = self.driver.find_element(*locator)
        locator.click()
        locator.send_keys(U.keys.CLEAR)

    def get_element_size(self, locator):
        div = self.driver.find_element(*locator)
        amount = list(div.find_elements(U.By.TAG_NAME, 'a'))
        size = len(amount)
        return size

    def get_css(self, locator, value):
        css = self.driver.find_element(*locator)
        val = css.value_of_css_property(value)
        return val

    # HEADER AND WELCOME LOCATORS #

    STORE_WELCOME = (U.By.CLASS_NAME, 'store_interestContainer')
    STORE_WELCOME_DISMISS = (U.By.CLASS_NAME, 'store_saveBtn')
    HEADER_LOGO = (U.By.CLASS_NAME, 'header_logo')
    HEADER_SEARCH_BAR = (U.By.CLASS_NAME, 'mainSearch_search')
    HEADER_SEARCH_LIST = (U.By.CLASS_NAME, 'mainSearch_list')
    HEADER_LOGIN = (U.By.CLASS_NAME, 'header_userAreaLink')
    HEADER_LOGOUT = (U.By.CSS_SELECTOR, '.header_logOut')

    # SECURITY LOCATORS

    FIRST_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[1]/span/input')
    SECOND_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[2]/span/input')
    THIRD_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[3]/span/input')
    FOURTH_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[4]/span/input')
    FIFTH_NUMBER = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/div[1]/div[5]/span/input')
    SUBMIT_CONFIRMATION = (U.By.XPATH, '/html/body/div[1]/div/div[4]/div/div/div/div/form/input')

    def click_login_signup(self):
        self.wait_for_clickable(Commons.HEADER_LOGIN).click()

    def click_logout(self):
        U.sleep(1)
        self.wait_for(Commons.HEADER_LOGOUT).click()

    # USED TO SUBMIT THE SECURITY CONFIRMATION CODE :)

    def click_submit_confirmation(self):
        self.wait_for_clickable(Commons.SUBMIT_CONFIRMATION).click()

    # TO BE USED ONLY IN THE SECURITY CODE PAGE - INSERTS THE SECURITY CODE STRAIGHT FROM THE DB - IT ALSO RETURNS IT FOR LATER USE (MAYBE)

    def insert_security_code(self, phone_number, false_flag):
        self.wait_for(Commons.SUBMIT_CONFIRMATION)
        requests = R.MongoRequests()
        login_code = requests.find_login_code(phone_number)
        signup_list = [
            Commons.FIRST_NUMBER,
            Commons.SECOND_NUMBER,
            Commons.THIRD_NUMBER,
            Commons.FOURTH_NUMBER,
            Commons.FIFTH_NUMBER
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
        Commons.click_submit_confirmation(self)
        return login_code

    @staticmethod
    def randomusrpswd():
        number = U.string.digits
        letter = U.string.ascii_letters
        special = '!@#$%^&*'
        letter_up = U.string.ascii_letters.upper()
        letters = (''.join(U.random.choice(letter) for _ in range(4)))
        specials = (''.join(U.random.choice(special) for _ in range(3)))
        numero = (''.join(U.random.choice(number) for _ in range(2)))
        upper = (''.join(U.random.choice(letter_up) for _ in range(3)))
        return f'{letters}{numero}{specials}{upper}'

    @staticmethod
    def random_mail():
        letter = U.string.ascii_letters
        letters = (''.join(U.random.choice(letter) for _ in range(7)))
        return f'{letters}@Bmail.com'

    @staticmethod
    def random_usr_name():
        letter = U.string.ascii_letters
        letters = (''.join(U.random.choice(letter) for _ in range(8)))
        return f'{letters}'

    @staticmethod
    def random_phone_number():
        nums = U.string.digits
        phone_number = (''.join(U.random.choice(nums) for _ in range(7)))
        return f'057{phone_number}'

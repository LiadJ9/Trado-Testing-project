from Project_folder.pages.Utils import TRADO_UTILS as U


class Commons(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = U.wdw(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(U.ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(U.ec.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        return self._wait.until(U.ec.invisibility_of_element(locator))

    def wait_for_window_number_to_change(self, num):
        return self._wait.until(U.ec.number_of_windows_to_be(num))

    def wait_for_url_change(self, url):
        return self._wait.until(U.ec.url_to_be(url))

    def wait_for_alert(self):
        return self._wait.until(U.ec.alert_is_present())

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_many(self, locator):
        return self.driver.find_elements(*locator)

    def insert(self, locator, insertion):
        locator = self.driver.find_element(*locator)
        locator.send_keys(insertion)

    # HEADER AND WELCOME LOCATORS #

    STORE_WELCOME = (U.By.CLASS_NAME, 'store_interestContainer')
    STORE_WELCOME_DISMISS = (U.By.CLASS_NAME, 'store_saveBtn')
    HEADER_LOGO = (U.By.CLASS_NAME, 'header_logo')
    HEADER_SEARCH_BAR = (U.By.CLASS_NAME, 'mainSearch_search')
    HEADER_SEARCH_LIST = (U.By.CLASS_NAME, 'mainSearch_list')
    HEADER_LOGIN = (U.By.CLASS_NAME, 'header_userAreaLink')

    def click_login_signup(self):
        self.wait_for_clickable(Commons.HEADER_LOGIN)
        self.find(Commons.HEADER_LOGIN).click()


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
        phone_number = (''.join(U.random.choice(nums) for _ in range(9)))
        return f'0{phone_number}'

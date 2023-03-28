import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


class CheckoutPage(Commons):

    CLICK_PAYMENT = (U.By.CSS_SELECTOR, '.button_button')
    CONTINUE_WITH_ORDER = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[3]/span[2]')
    BUSINESS_NAME = (U.By.CSS_SELECTOR, '.checkout-form_checkoutUserForm > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
    BUSINESS_ID = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[2]/input')
    MAIL = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[3]/input')
    STREET = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[2]/input')
    CITY = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[1]/input')
    HOUSE_NUM = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[3]/input')
    ENTRENCE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[4]/input')
    FLOOR = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div[5]/input')
    CONTACT_NAME = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[1]/input')
    FIRST_NAME = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[2]/input')
    LAST_NAME = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[2]/div[3]/input')
    FINISH_PURCHASE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[3]/div[3]/button/input')
    CREDIT_CARD = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[2]/div/div/div')
    CREDIT_CARD_NUMBER = (U.By.XPATH, '//*[@id="credit-card-input"]')
    CREDIT_CARD_ID = (U.By.CSS_SELECTOR, '#userId-input')
    CREDIT_CARD_EXPIRE_MONTH = (U.By.ID, 'expmonth')
    FIFTH_MONTH = (U.By.XPATH, '/html/body/form/div[3]/fieldset/div[3]/div[1]/select/option[6]')
    CREDIT_CARD_EXPIRE_YEAR = (U.By.ID, 'expyear')
    YEAR_24 = (U.By.XPATH, '/html/body/form/div[3]/fieldset/div[3]/div[2]/select/option[3]')
    CVC = (U.By.ID, 'cvv')
    SAVE_CARD = (U.By.ID, 'btnSubmit')
    PLACE_ORDER_FINAL = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[2]/div[3]/button')
    ORDER_CONFIRMED = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div')
    CREDIT_CARD_POP_UP = (U.By.CSS_SELECTOR, '#yaadFrame')
    DETAILS_ERR_MESSAGE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/form/section[1]/div[1]/div[3]/div[2]')
    AMOUNT_OF_ITEM = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/input')

    def click_checkout(self):
        self.wait_for(CheckoutPage.CLICK_PAYMENT).click()

    def click_continue_order(self):
        self.wait_for(CheckoutPage.CONTINUE_WITH_ORDER).click()

    def fill_out_form(self, business_name, business_id, mail, street, city, house_num, entrence, floor, contact, first_name, last_name):
        U.sleep(1)
        self.clear(CheckoutPage.BUSINESS_NAME)
        self.insert(CheckoutPage.BUSINESS_NAME, business_name)
        U.sleep(1)
        self.clear(CheckoutPage.BUSINESS_ID)
        self.insert(CheckoutPage.BUSINESS_ID, business_id)
        U.sleep(1)
        self.clear(CheckoutPage.MAIL)
        self.insert(CheckoutPage.MAIL, mail)
        U.sleep(2)
        self.clear(CheckoutPage.STREET)
        self.insert(CheckoutPage.STREET, street)
        U.sleep(1)
        self.clear(CheckoutPage.CITY)
        self.insert(CheckoutPage.CITY, city)
        U.sleep(1)
        self.clear(CheckoutPage.HOUSE_NUM)
        self.insert(CheckoutPage.HOUSE_NUM, house_num)
        U.sleep(1)
        self.clear(CheckoutPage.ENTRENCE)
        self.insert(CheckoutPage.ENTRENCE, entrence)
        U.sleep(1)
        self.clear(CheckoutPage.FLOOR)
        self.insert(CheckoutPage.FLOOR, floor)
        U.sleep(1)
        self.clear(CheckoutPage.CONTACT_NAME)
        self.insert(CheckoutPage.CONTACT_NAME, contact)
        U.sleep(1)
        self.clear(CheckoutPage.FIRST_NAME)
        self.insert(CheckoutPage.FIRST_NAME, first_name)
        self.insert(CheckoutPage.BUSINESS_NAME, 'blarg')
        self.clear(CheckoutPage.LAST_NAME)
        self.insert(CheckoutPage.LAST_NAME, last_name)
        U.sleep(1)
        self.wait_for(CheckoutPage.FINISH_PURCHASE).click()

    def go_to_credit_card_page(self):
        U.sleep(3)
        self.wait_for(CheckoutPage.CREDIT_CARD).click()
        U.sleep(1)

    def click_already_filled_form(self):
        self.wait_for(CheckoutPage.FINISH_PURCHASE).click()

    def find_frame(self):
        frame = self.find(CheckoutPage.CREDIT_CARD_POP_UP)
        return frame

    def add_credit_card(self):
        U.sleep(4)
        self.insert(CheckoutPage.CREDIT_CARD_NUMBER, '4580000000000000')
        U.sleep(1)
        self.insert(CheckoutPage.CREDIT_CARD_ID, '326815909')
        U.sleep(1)
        self.wait_for(CheckoutPage.CREDIT_CARD_EXPIRE_MONTH).click()
        U.sleep(1)
        self.wait_for(CheckoutPage.FIFTH_MONTH).click()
        self.wait_for(CheckoutPage.CREDIT_CARD_EXPIRE_YEAR).click()
        U.sleep(1)
        self.wait_for(CheckoutPage.YEAR_24).click()
        self.insert(CheckoutPage.CVC, '123')
        U.sleep(5)
        self.wait_for(CheckoutPage.SAVE_CARD).click()
        self.wait_for(CheckoutPage.PLACE_ORDER_FINAL).click()

    def assert_order_confirmed(self):
        assert self.wait_for(CheckoutPage.ORDER_CONFIRMED)

    def assert_invalid_details_message(self):
        assert self.wait_for(CheckoutPage.DETAILS_ERR_MESSAGE)

    def order_2000_items(self):
        U.sleep(1)
        self.insert(CheckoutPage.AMOUNT_OF_ITEM, '2000')

    def place_order(self):
        self.wait_for(CheckoutPage.PLACE_ORDER_FINAL).click()



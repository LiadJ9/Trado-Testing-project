import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


class PersonalPage(Commons):

    CONTACT_LINK_PRODUCTS = (U.By.CSS_SELECTOR, '.userProducts_userProductsList > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)')
    CONTACT_LINK_EWALLET = (U.By.CSS_SELECTOR, '.userWallet_userWallet > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)')
    CONTACT_LINK_PREVIOUS_ORDERS = (U.By.CSS_SELECTOR, 'div.userOrders_userOrders:nth-child(3) > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)')
    CONTACT_LINK_ORDERS_TODO = (U.By.CSS_SELECTOR, 'div.userOrders_userOrders:nth-child(4) > div:nth-child(3) > span:nth-child(1) > a:nth-child(1)')
    FIRST_NAME = (U.By.CSS_SELECTOR, 'div.false:nth-child(1) > span:nth-child(2) > input:nth-child(1)')
    E_WALLET_BTN = (U.By.CSS_SELECTOR, '.button_button')

    def click_(self, locator):
        self.wait_for(locator).click()

    def assert_in_support(self):
        assert self.driver.current_url == 'https://qa.trado.co.il/contact'
        self.driver.get('https://qa.trado.co.il/user/personalArea')

    def inserting_info(self):
        self.insert(PersonalPage.FIRST_NAME, 'Test_name')
from Project_folder.pages.common_page import Commons
import Project_folder.pages.Utils.TRADO_UTILS as U


class FooterPage(Commons):
    # STAY IN TOUCH
    FACEBOOK = (U.By.CSS_SELECTOR, '.footer_contact > a:nth-child(2)')
    INSTAGRAM = (U.By.CSS_SELECTOR, '.footer_contact > a:nth-child(3)')
    TWITTER = (U.By.CSS_SELECTOR, '.footer_contact > a:nth-child(4)')
    # ADDITIONALS
    FAQ = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(2) > a:nth-child(2)')
    SHIPMENT = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(2) > a:nth-child(3)')
    PAYMENT_SOLUTION = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(2) > a:nth-child(4)')
    MAX_BUSINESS = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(2) > a:nth-child(5)')
    # IMPORTANTS
    WHO_ARE_WE = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(1) > a:nth-child(2)')
    PERSONAL_AREA = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(1) > a:nth-child(3)')
    E_WALLET = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(1) > a:nth-child(4)')
    CONTACT_US = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(1) > a:nth-child(5)')
    BUSINESS_INTERFACE = (U.By.CSS_SELECTOR, '.footer_linkWrapper > div:nth-child(1) > a:nth-child(6)')
    # LEGAL INFORMATION
    USE_REGULATIONS = (U.By.CSS_SELECTOR, '.footer_copyrightsContainer > div:nth-child(2) > a:nth-child(1)')
    PRIVACY_POLICY = (U.By.CSS_SELECTOR, '.footer_copyrightsContainer > div:nth-child(2) > a:nth-child(2)')
    ACCESSIBILITY = (U.By.CSS_SELECTOR, '.footer_copyrightsContainer > div:nth-child(2) > a:nth-child(3)')

    def click_facebook(self):
        self.wait_for_clickable(self.FACEBOOK).click()

    def click_instagram(self):
        self.wait_for_clickable(self.INSTAGRAM).click()

    def click_twitter(self):
        self.wait_for_clickable(self.TWITTER).click()

    def click_faq(self):
        self.wait_for_clickable(self.FAQ).click()

    def click_shipment(self):
        self.wait_for_clickable(self.SHIPMENT).click()

    def click_payment(self):
        self.wait_for_clickable(self.PAYMENT_SOLUTION).click()

    def click_max_business(self):
        self.wait_for_clickable(self.MAX_BUSINESS).click()

    def click_who_are_we(self):
        self.wait_for_clickable(self.WHO_ARE_WE).click()

    def click_personal_area(self):
        self.wait_for_clickable(self.PERSONAL_AREA).click()

    def click_e_wallet(self):
        self.wait_for_clickable(self.E_WALLET).click()

    def click_contact_us(self):
        self.wait_for_clickable(self.CONTACT_US).click()

    def click_business_interface(self):
        self.wait_for_clickable(self.BUSINESS_INTERFACE).click()

    def click_use_regulations(self):
        self.wait_for_clickable(self.USE_REGULATIONS).click()

    def click_privacy_policy(self):
        self.wait_for_clickable(self.PRIVACY_POLICY).click()

    def click_accessibility(self):
        self.wait_for_clickable(self.ACCESSIBILITY).click()



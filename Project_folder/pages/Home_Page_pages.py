from Project_folder.pages.common_page import Commons
import Project_folder.pages.Utils.TRADO_UTILS as U
import re


class HomePage(Commons):

    # Home Page locators

    UPLOAD_NEW_PRODUCT = (U.By.CSS_SELECTOR, 'a.verticalMenu_addProduct:nth-child(1) > span:nth-child(1)')
    UP_BUSINESS_NAME = (U.By.CSS_SELECTOR, 'div.form_items:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2) > input:nth-child(1)')
    FAQ_REDIRECT = (U.By.CSS_SELECTOR, 'div.cardInfo_cardInfo:nth-child(3) > div:nth-child(7) > a:nth-child(1)')
    CONTACT_US_REDIRECT = (U.By.CSS_SELECTOR, 'div.cardInfo_cardInfo:nth-child(4) > div:nth-child(5) > a:nth-child(1)')
    SHIPMENT_REDIRECT = (U.By.CSS_SELECTOR, 'div.cardInfo_cardInfo:nth-child(5) > div:nth-child(6) > a:nth-child(1)')
    SORT_ORDER_TAB = (U.By.CSS_SELECTOR, '.select_select > select:nth-child(1)')
    SORT_ORDER_POPULAR = (U.By.CSS_SELECTOR, '.select_select > select:nth-child(1) > option:nth-child(1)')
    SORT_LOW_TO_HIGH = (U.By.CSS_SELECTOR, '.select_select > select:nth-child(1) > option:nth-child(2)')
    SORT_HIGH_TO_LOW = (U.By.CSS_SELECTOR, '.select_select > select:nth-child(1) > option:nth-child(3)')
    SORT_GRID = (U.By.CSS_SELECTOR, '.micon-squares-o')
    SORT_ROWS = (U.By.CSS_SELECTOR, '.micon-lines-o')
    FIRST_PRODUCT_PRICE = (U.By.CSS_SELECTOR, '.productsList_list > a:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
    ITEM_LIST = (U.By.CSS_SELECTOR, '.productsList_list')
    PRODUCT_COUNT = (U.By.CSS_SELECTOR, '.productsList_title')
    CAROUSEL_LEFT = (U.By.CSS_SELECTOR, 'button.control-arrow:nth-child(1)')
    CAROUSEL_RIGHT = (U.By.CSS_SELECTOR, 'button.control-arrow:nth-child(3)')
    YELLOW_SLIDE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[5]/a')
    MAX_SLIDE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[2]/a')
    MAX_VISIBILITY = (U.By.CSS_SELECTOR, '.modal_content > div:nth-child(1) > div:nth-child(1) > img:nth-child(2)')
    BROWN_SLIDE = (U.By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/ul/li[8]/a')

    def click_upload_new_product(self):
        self.wait_for(HomePage.UPLOAD_NEW_PRODUCT).click()

    def click_faq_redirect(self):
        self.wait_for(HomePage.FAQ_REDIRECT).click()

    def click_contact_us_redirect(self):
        self.wait_for(HomePage.CONTACT_US_REDIRECT).click()

    def click_shipment_redirect(self):
        self.wait_for(HomePage.SHIPMENT_REDIRECT).click()

    def click_carousel(self, tleft_rightf):
        if tleft_rightf:
            self.wait_for(HomePage.CAROUSEL_LEFT).click()
        else:
            self.wait_for(HomePage.CAROUSEL_RIGHT).click()

    def click_max_slide(self):
        self.wait_for(HomePage.MAX_SLIDE).click()

    def click_brown_slide(self):
        self.wait_for(HomePage.BROWN_SLIDE).click()

    def select_sorting(self, sortchoice):
        self.wait_for(HomePage.SORT_ORDER_TAB).click()
        if sortchoice == 'popular':
            return self.wait_for(HomePage.SORT_ORDER_POPULAR).click()
        elif sortchoice == 'high':
            return self.wait_for(HomePage.SORT_HIGH_TO_LOW).click()
        elif sortchoice == 'low':
            return self.wait_for(HomePage.SORT_LOW_TO_HIGH).click()

    def select_sorting_ux(self, sort_choice):
        if sort_choice == 'grid':
            self.wait_for(HomePage.SORT_GRID).click()
        elif sort_choice == 'row':
            self.wait_for(HomePage.SORT_ROWS).click()

    def get_display(self):
        foo = self.get_css(HomePage.ITEM_LIST, 'display')
        return foo

    def get_first_product_price(self):
        self.wait_for(HomePage.FIRST_PRODUCT_PRICE)
        valued_price = self.get_text(HomePage.FIRST_PRODUCT_PRICE)
        valued_price = re.findall(r'\d+\.\d+', f'{valued_price}')
        for i in valued_price:
            num = i
            return float(num)
        return valued_price

    def get_item_list_size(self):
        self.wait_for(HomePage.FIRST_PRODUCT_PRICE)
        size = self.get_element_size(HomePage.ITEM_LIST)
        return size

    def get_product_count(self):
        self.wait_for(HomePage.PRODUCT_COUNT)
        txt = self.get_text(HomePage.PRODUCT_COUNT)
        count = re.findall(r'\d+', f'{txt}')
        for i in count:
            num = i
            return int(num)

    def wait_for_slide(self, slide):
        slides = self.find(slide)
        while not slides.is_displayed():
            self.click_carousel(True)
        U.sleep(1)

    def max_visibility(self):
        maxs = self.find(HomePage.MAX_VISIBILITY)
        return maxs.is_displayed()









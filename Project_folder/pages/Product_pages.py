import random
import re
import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


class ProductPage(Commons):

    PRODUCT_A = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[5]')
    PRODUCT_B = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[4]')
    PRODUCT_C = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]')
    ADD_PRODUCT = (U.By.CSS_SELECTOR, '.micon-plus')
    REMOVE_PRODUCT = (U.By.CSS_SELECTOR, '.micon-minus')
    CART_LIST = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div')
    PRODUCT_ID = (U.By.CSS_SELECTOR, '.fullProduct_imageW > div:nth-child(2)')
    UNITS_PER_CARTON = (U.By.CSS_SELECTOR, 'div.fullProduct_infoCard:nth-child(2) > div:nth-child(1)')
    PRICE_PER_CARTON = (U.By.CSS_SELECTOR, 'div.fullProduct_infoCard:nth-child(3) > div:nth-child(1)')
    STOCK_AMOUNT = (U.By.CSS_SELECTOR, 'div.fullProduct_infoCard:nth-child(1) > div:nth-child(1)')
    CLEAR_CART = (U.By.CSS_SELECTOR, '.cart_clearCart')
    ADD_PRODUCT_IN_CART = (U.By.CSS_SELECTOR, 'div.productBtn_productBtn:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > i:nth-child(1)')
    UNITS_IN_CART = (U.By.CSS_SELECTOR, '.inlineProduct_units > div:nth-child(1)')
    CARTONS_IN_CART = (U.By.CSS_SELECTOR, '.inlineProduct_units > div:nth-child(3)')
    CART_ITEM_PRICE = (U.By.CSS_SELECTOR, '.inlineProduct_price > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
    SUM_BEFORE_TAX = (U.By.CSS_SELECTOR, '.cart_prices > h6:nth-child(1) > span:nth-child(2)')
    SUM_AFTER_TAX = (U.By.CSS_SELECTOR, '.cart_prices > h6:nth-child(4) > span:nth-child(2)')
    TAX_RATE = (U.By.CSS_SELECTOR, '.cart_prices > h6:nth-child(3) > span:nth-child(2)')

    def click_(self, locator):
        self.wait_for(locator).click()

    def select_random_product(self):
        prod_list = [
            ProductPage.PRODUCT_B,
            ProductPage.PRODUCT_A,
            ProductPage.PRODUCT_C
        ]
        random_product = random.choice(prod_list)
        self.wait_for(random_product).click()

    def get_cart_list_size(self):
        self.wait_for(ProductPage.CART_LIST)
        size = self.get_element_size(ProductPage.CART_LIST)
        return size

    def get_number(self, locator):
        self.wait_for(locator)
        txt = self.get_text(locator)
        count = re.findall(r'\d+', f'{txt}')
        for i in count:
            num = i
            return int(num)

    def get_decimal_number(self, locator):
        self.wait_for(locator)
        txt = self.get_text(locator)
        count = re.findall(r'\d+\.\d+', f'{txt}')
        for i in count:
            num = i
            return float(num)

    def clear_cart(self):
        self.wait_for(ProductPage.CLEAR_CART).click()

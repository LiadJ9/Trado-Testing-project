import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons
import random


class SearchPages(Commons):
    SEARCHBAR = (U.By.CSS_SELECTOR, 'input.mainSearch_search')
    LEMON_KUSH_OIL = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[4]/div/div[2]/div[2]/div[1]')
    ACADIA = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[5]/div/div[2]/div[2]/div[1]')
    OG_KUSH = (U.By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/a[3]/div/div[2]/div[2]/div[1]')
    LEMON_KUSH_FROM_SEARCH = (U.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[@href="/product/59996"]')
    OG_KUSH_FROM_SEARCH = (U.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[@href="/product/67373"]')
    ACADIA_FROM_SEARCH = (U.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[@href="/product/56586"]')
    PRODUCT_TO_CLICK = (U.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]/div/a[1]/div/div[2]')
    SEARCHBAR_HANDLER = (U.By.XPATH, '/html/body/div/div/div[2]/header/div/div/div/div[1]')

    def click_(self, locator):
        self.wait_for(locator).click()

    def search(self, search_term):
        self.click_(self.SEARCHBAR)
        U.sleep(1)
        self.insert(SearchPages.SEARCHBAR, search_term)
        U.sleep(2)

    def select_random_product(self):
        prod_list = [
            SearchPages.LEMON_KUSH_OIL,
            SearchPages.ACADIA,
            SearchPages.OG_KUSH
        ]
        rnd = random.choice(prod_list)
        rnd_txt = self.get_text(rnd)
        return rnd_txt

    def assert_searched_product_is_shown(self, product_name):
        if product_name == 'שמן למון קוש':
            assert self.wait_for(SearchPages.LEMON_KUSH_FROM_SEARCH)
        elif product_name == 'אקדיה':
            assert self.wait_for(SearchPages.ACADIA_FROM_SEARCH)
        elif product_name == 'OG Kush':
            assert self.wait_for(SearchPages.OG_KUSH_FROM_SEARCH)





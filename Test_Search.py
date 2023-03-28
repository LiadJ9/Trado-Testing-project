import pytest
import Project_folder.pages.Search_pages as S
import Project_folder.pages.Product_pages as P
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Search')
@allure.id(32)
@allure.title('Searching for random item')
@allure.description('Searching for random item will correctly show the item and relevant searches')
@allure.severity(allure.severity_level.NORMAL)
def test_search_bar(driver):
    search = S.SearchPages(driver)
    with allure.step('Getting random product name'):
        rnd_txt = search.select_random_product()
    with allure.step('searching random product'):
        search.search(rnd_txt)
    with allure.step('asserting random product is in list'):
        search.assert_searched_product_is_shown(rnd_txt)


@allure.epic('Test Search')
@allure.id(35)
@allure.title('Clicking item in search bar')
@allure.description('Clicking on the item in the search box will redirect to the relevant item')
@allure.severity(allure.severity_level.NORMAL)
def test_clicking_searched_item(driver):
    search = S.SearchPages(driver)
    with allure.step('Searching for שמן'):
        search.search('ש')
        search.search('מן')
    with allure.step('clicking desired product'):
        search.click_(search.PRODUCT_TO_CLICK)
    with allure.step('asserting we reached product page'):
        assert driver.current_url == "https://qa.trado.co.il/product/60341"



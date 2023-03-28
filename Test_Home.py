import pytest
import Project_folder.pages.Home_Page_pages as H
import Project_folder.pages.Login_Pages as L
import Project_folder.MongoDB_requests as R
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Home')
@allure.id(1)
@allure.title("Upload new product button functionality")
@allure.description('Verifying the functionality of the main add "add new products" button (login required)')
@allure.severity(allure.severity_level.CRITICAL)
def test_upload_product_button(driver):
    home = H.HomePage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Clicking and asserting we have reached the right place'):
        home.click_upload_new_product()
        assert driver.find_element(*home.UP_BUSINESS_NAME)


@allure.epic('Test Home')
@allure.id(2)
@allure.title("Upload new product")
@allure.description('Uploading a new product to the store and the process of ordering will work as intended: DB will also be updated.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
def test_upload_new_product(driver):
    var = False
    assert var


@allure.epic('Test Home')
@allure.id(3)
@allure.title("FAQ redirects works as intended")
@allure.description('Clicking on the "לכל השאלות" hyperlink will redirect me to the FAQ page')
@allure.severity(allure.severity_level.TRIVIAL)
def test_faq_redirect(driver):
    home = H.HomePage(driver)
    with allure.step('Clicking the link'):
        home.click_faq_redirect()
    with allure.step('Asserting correct redirect'):
        assert driver.current_url == 'https://qa.trado.co.il/questions'


@allure.epic('Test Home')
@allure.id(4)
@allure.title("Contact us redirects works as intended")
@allure.description('Clicking on the Contact us hyperlink will redirect me to the Contact us page')
@allure.severity(allure.severity_level.TRIVIAL)
def test_contact_us_redirect(driver):
    home = H.HomePage(driver)
    with allure.step('Clicking the link'):
        home.click_contact_us_redirect()
    with allure.step('Asserting correct redirect'):
        assert driver.current_url == 'https://qa.trado.co.il/contact'


@allure.epic('Test Home')
@allure.id(5)
@allure.title("Shipment redirects works as intended")
@allure.description('Clicking on the Shipment hyperlink will redirect me to the Shipment page')
@allure.severity(allure.severity_level.TRIVIAL)
def test_shipment_redirect(driver):
    home = H.HomePage(driver)
    with allure.step('Clicking the link'):
        home.click_shipment_redirect()
    with allure.step('Asserting correct redirect'):
        assert driver.current_url == 'https://qa.trado.co.il/shipment'


@allure.epic('Test Home')
@allure.id(6)
@allure.title('Product sorting categories display the correct information')
@allure.description('Switching between product sort order will change the products displayed and instead would sort them by the desired order(Popularity, low to high, high to low)')
def test_product_categories(driver):
    home = H.HomePage(driver)
    with allure.step('Clicking product sorting button and select low to high'):
        home.select_sorting('low')
    with allure.step('Getting the first item on the list (which should be the lowest -- under 100)'):
        lowest = home.get_first_product_price()
        assert float(lowest) <= 100.00


@allure.epic('Test Home')
@allure.id(7)
@allure.title('Product sorting Ux swapping (Between rows and tiles)')
@allure.description('Switching between product sorting by row by tiles will properly change display')
def test_product_ux_change(driver):
    home = H.HomePage(driver)
    with allure.step('Clicking on row item sorting'):
        home.select_sorting_ux('row')
    with allure.step('asserting display order has changed'):
        assert home.get_display() == 'block'
    with allure.step('Clicking on grid item sorting'):
        home.select_sorting_ux('grid')
    with allure.step('asserting display order has changed'):
        assert home.get_display() == 'grid'


@allure.epic('Test Home')
@allure.id(8)
@allure.title('Products listed == Products available')
@allure.description('Verify the amount of products listed is the actual amount of products available to click')
def test_product_count(driver):
    home = H.HomePage(driver)
    with allure.step('Asserting products listed == products available'):
        assert home.get_product_count() == home.get_item_list_size()


@allure.epic('Test Home')
@allure.id(9)
@allure.title('Highlights carousel arrows function as intended ')
@allure.description('clicking the left and right carousel arrows will change the current display')
def test_carousel_arrows(driver):
    home = H.HomePage(driver)
    with allure.step('clicking left and right in the carousel'):
        home.click_carousel(True)
        home.click_carousel(False)
    with allure.step('waiting until selected page shows up'):
        home.wait_for_slide(home.YELLOW_SLIDE)


@allure.epic('Test Home')
@allure.id(10)
@allure.title('Highlight carousel pages work as intended')
@allure.description('The featured pages in the Highlight carousel will redirect me to the appropriate page')
def test_carousel_pages(driver):
    home = H.HomePage(driver)
    login = L.LoginPage(driver)
    with allure.step('Clicking on carousel arrows until reaching desired page'):
        home.wait_for_slide(home.BROWN_SLIDE)
    with allure.step('Clicking the brown slide should get us to the login/signup page'):
        home.click_brown_slide()
    with allure.step('asserting we reached the right place'):
        assert login.find(login.PHONE_NUMBER)


@allure.epic('Test Home')
@allure.id(11)
@allure.title('MAX business - additional details page redirect ')
@allure.description('The max business additional details hyperlink will redirect me to the appropriate 3rd party page')
def test_carousel_max(driver):
    home = H.HomePage(driver)
    with allure.step('clicking on the carousel arrows until we reach the max slide'):
        home.wait_for_slide(home.MAX_SLIDE)
    with allure.step('Clicking on the MAX slide'):
        home.click_max_slide()
    with allure.step('Asserting we have reached the Max card pop-up'):
        assert home.max_visibility()


@allure.epic('Test Home')
@allure.id(34)
@allure.title('Highlight carousel pages work as intended (Logged in)')
@allure.description('The featured pages in the Highlight carousel will redirect me to the appropriate page')
def test_carousel_pages(driver):
    home = H.HomePage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Clicking on carousel arrows until reaching desired page'):
        home.wait_for_slide(home.BROWN_SLIDE)
    with allure.step('Clicking the brown slide should get us to the login/signup page'):
        home.click_brown_slide()
    with allure.step('asserting we reached the right place'):
        assert login.find(login.PHONE_NUMBER)


@allure.epic('Test Home')
@allure.id(33)
@allure.title('Products listed == Products in DB')
@allure.description('Verifying that the amount of products listed as available is number of products in db')
def test_product_count_in_db(driver):
    home = H.HomePage(driver)
    requests = R.MongoRequests()
    with allure.step('Asserting products listed == products in DB'):
        assert home.get_item_list_size() == requests.get_product_count()


@allure.epic('Test Home')
@allure.id(59)
@allure.title('Product sorting categories display the correct information (Logged in)')
@allure.description('Switching between product sort order will change the products displayed and instead would sort them by the desired order(Popularity, low to high, high to low)')
def test_product_categories_login(driver):
    home = H.HomePage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Clicking product sorting button and select low to high'):
        home.select_sorting('low')
    with allure.step('Getting the first item on the list (which should be the lowest -- under 100)'):
        lowest = home.get_first_product_price()
        assert float(lowest) <= 100.00

import pytest
import Project_folder.pages.Personal_Pages as P
import Project_folder.pages.Login_Pages as L
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Personal Area')
@allure.id(36)
@allure.title("Test Support Hyperlinks")
@allure.description('Verify that the 4 support links in the personal area page redirect to the right page')
@allure.severity(allure.severity_level.MINOR)
def test_click_support_links(driver):
    personal = P.PersonalPage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Navigating to Personal area'):
        login.click_login_signup()
    with allure.step('Clicking and asserting all 4 links'):
        personal.click_(personal.CONTACT_LINK_PRODUCTS)
        personal.assert_in_support()
        personal.click_(personal.CONTACT_LINK_EWALLET)
        personal.assert_in_support()
        personal.click_(personal.CONTACT_LINK_ORDERS_TODO)
        personal.assert_in_support()
        personal.click_(personal.CONTACT_LINK_PREVIOUS_ORDERS)
        personal.assert_in_support()


@allure.epic('Test Personal Area')
@allure.id(37)
@allure.title("Filling in delivery details")
@allure.description('Using and filling in the delivery details section will work as intended')
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_in_delivery_info(driver):
    personal = P.PersonalPage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Navigating to Personal area'):
        login.click_login_signup()
    with allure.step('Filling in personal details'):
        personal.inserting_info()
        # CANNOT CONTINUE TEST -- ELEMENTS ARE NOT INTERACTIBLE


@allure.epic('Test Personal Area')
@allure.id(38)
@allure.title("e-wallet 'pull' button")
@allure.description('Using the "Pull" button will redirect to the appropriate page(I don"t know which page because nothing in this site works)')
@allure.severity(allure.severity_level.NORMAL)
def test_e_wallet_pull(driver):
    personal = P.PersonalPage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('Navigating to Personal area'):
        login.click_login_signup()
    with allure.step('clicking e-wallet'):
        personal.click_(personal.E_WALLET_BTN)
    with allure.step('Asserting we reached the E_wallet page'):
        assert driver.current_url == 'https://qa.trado.co.il/wallet'


@allure.epic('Test Personal Area')
@allure.id(39)
@allure.title("previous orders section")
@allure.description('Previous orders section will correctly show previous orders')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(condition=lambda: True, reason='NO WAY TO TEST THIS RIGHT NOW')
def test_previous_orders_section(driver):
    assert False




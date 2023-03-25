import allure
import pytest
import Project_folder.pages.Footer_pages as F


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Footers')
@allure.id(40)
@allure.title('Verify Stay in touch - Facebook')
@allure.description("Facebook link will redirect to trado's facebook page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_verify_facebook(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking the facebook link'):
        footer.click_facebook()
    with allure.step('switching to facebook tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://www.facebook.com/')
    with allure.step("Closing the facebook tab - cleanup"):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(41)
@allure.title('Verify Stay in touch - Instagram')
@allure.description("Instagram link will redirect to trado's instagram page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_verify_instagram(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking on the instagram link'):
        footer.click_instagram()
    with allure.step('Switching to the instagram tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://www.instagram.com/')
    with allure.step('Closing the instagram tab - cleanup'):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(42)
@allure.title('Verify Stay in touch - Twitter')
@allure.description("Twitter link will redirect to trado's Twitter page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_verify_twitter(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking on the twitter link'):
        footer.click_twitter()
    with allure.step('Switching to the twitter tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://twitter.com/?lang=he')
    with allure.step('Closing the twitter tab - cleanup'):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(43)
@allure.title('Additionals - Common questions')
@allure.description("Common questions link will redirect to trado's FAQ page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_faq_link(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on faq link'):
        footer.click_faq()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/questions'


@allure.epic('Test Footers')
@allure.id(44)
@allure.title('Additionals - How does our shipment work?')
@allure.description("shipment link will redirect to trado's shipment info page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_shipment_link(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on shipment link'):
        footer.click_shipment()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/shipment'


@allure.epic('Test Footers')
@allure.id(45)
@allure.title('Additionals - Payment solutions')
@allure.description("Payment solutions link will redirect to the third party MAX page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_payment_solutions(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking on the payment solutions link'):
        footer.click_payment()
    with allure.step('Switching to the third party tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://www.max.co.il/cards/card/8649')
    with allure.step('Closing the MAX tab - cleanup'):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(46)
@allure.title('Additionals - Business solutions')
@allure.description("Business solutions link will redirect to the third party MAX page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_business_solutions(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking on the Business solutions link'):
        footer.click_max_business()
    with allure.step('Switching to the third party tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://www.max.co.il/cards/card/8649')
    with allure.step('Closing the MAX tab - cleanup'):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(47)
@allure.title('Importants - Who we are')
@allure.description("Who we are link will redirect to the site information page")
@allure.severity(allure.severity_level.MINOR)
def test_who_we_are(driver):
    footer = F.FooterPage(driver)
    common = F.Commons(driver)
    trado_store = driver.current_window_handle
    with allure.step('Clicking on the who are we link'):
        footer.click_who_are_we()
    with allure.step('Switching to the information page tab'):
        common.switch_tabs(trado_store)
    with allure.step('Asserting URL is correct'):
        assert common.wait_for_url_change('https://www.trado.co.il/page')
    with allure.step('Closing the information tab - cleanup'):
        driver.close()
        driver.switch_to.window(trado_store)


@allure.epic('Test Footers')
@allure.id(48)
@allure.title('Importants - My account')
@allure.description("My account link will redirect to trado's personal area page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_my_account(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on My account link'):
        footer.click_personal_area()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/user/personalArea'


@allure.epic('Test Footers')
@allure.id(49)
@allure.title('Importants- eTrado')
@allure.description("e-trado link  will redirect to trado's e-wallet page")
@allure.severity(allure.severity_level.MINOR)
def test_e_trado(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on E-wallet link'):
        footer.click_e_wallet()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/etrado'


@allure.epic('Test Footers')
@allure.id(50)
@allure.title('Importants- Contact Us')
@allure.description("Contact us link  will redirect to trado's Contact us page")
@allure.severity(allure.severity_level.TRIVIAL)
def test_contact_us(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on Contact us link'):
        footer.click_contact_us()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/contact'


@allure.epic('Test Footers')
@allure.id(51)
@allure.title('Importants- Join us')
@allure.description("Join us link will redirect to the New business page")
@allure.severity(allure.severity_level.MINOR)
def test_join_us(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on Join us link'):
        footer.click_business_interface()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/joinUs'


@allure.epic('Test Footers')
@allure.id(52)
@allure.title('Privacy policy link')
@allure.description("Privacy policy link will redirect to the Privacy policy page")
@allure.severity(allure.severity_level.NORMAL)
def test_privacy_policy(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on Privacy policy link'):
        footer.click_privacy_policy()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/info/%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA'


@allure.epic('Test Footers')
@allure.id(53)
@allure.title('Website accessibility link')
@allure.description("Website accessibility link will redirect to the Accessibility page")
@allure.severity(allure.severity_level.NORMAL)
def test_accessibility(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on Accessibility link'):
        footer.click_accessibility()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/info/%D7%94%D7%A6%D7%94%D7%A8%D7%AA%20%D7%A0%D7%92%D7%99%D7%A9%D7%95%D7%AA'


@allure.epic('Test Footers')
@allure.id(54)
@allure.title('Website Use regulations link')
@allure.description("Use regulations link will redirect to the Use regulations page")
@allure.severity(allure.severity_level.NORMAL)
def test_use_regulations(driver):
    footer = F.FooterPage(driver)
    with allure.step('Clicking on regulations link'):
        footer.click_use_regulations()
    with allure.step('Asserting URL has changed'):
        assert driver.current_url == 'https://qa.trado.co.il/info/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F'







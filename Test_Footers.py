import allure
import pytest
import Project_folder.pages.Footer_pages as F
import Project_folder.pages.common_page as C

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
    footer.click_facebook()
    common.wait_for_window_number_to_change(2)
    for facebook in driver.window_handles:
        if facebook != trado_store:
            driver.switch_to.window(facebook)
            break
    # Asserting facebook has opened
    assert common.wait_for_url_change('https://www.facebook.com/')
    driver.close()
    driver.switch_to.window(trado_store)


def test_verify_instagram(driver):
    footer = F.FooterPage(driver)


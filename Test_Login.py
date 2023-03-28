import pytest
import Project_folder.pages.Registration_pages as Rp
import Project_folder.pages.Login_Pages as L
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Login')
@allure.id(12)
@allure.title("Log in with existing account - security valid")
@allure.description('The intended way to log into an existing account')
@allure.severity(allure.severity_level.CRITICAL)
def test_log_in_with_valid_info(driver):
    signup = Rp.SignupPage(driver)
    login = L.LoginPage(driver)
    common = L.Commons(driver)
    with allure.step('Creating the valid account'):
        phone_number, login_code = signup.sign_up(True, True, True, True, True, True, False)
    with allure.step('Logging out of the created account'):
        common.click_logout()
    with allure.step('Logging into new account'):
        login.log_in(phone_number, True, False)
    with allure.step('Asserting user has logged in'):

        txt = common.get_text(common.HEADER_LOGIN)
        assert txt == 'שלום ,\nאזור אישי'


@allure.epic('Test Login')
@allure.id(13)
@allure.title("Log in with existing account - security invalid")
@allure.description('Invalid security error will pop up')
@allure.severity(allure.severity_level.CRITICAL)
def test_log_in_invalid_security(driver):
    login = L.LoginPage(driver)
    with allure.step('Logging into account with invalid security code'):
        login.log_in('0000000000', False, True)
    with allure.step('Asserting error message'):
        error = login.find_error()
        assert error == 'Failed To Login'


@allure.epic('Test Login')
@allure.id(14)
@allure.title("Log in with non-existing account - security invalid")
@allure.description('Invalid account error will show up')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_log_in_invalid_details(driver):
    login = L.LoginPage(driver)
    with allure.step('Trying to log into non existing account'):
        login.log_in('jjjjjjjjjj', True, False)


@allure.epic('Test Login')
@allure.id(15)
@allure.title('Log in with Twitter account')
@allure.description('The twitter login page will show up - redirecting through 3rd party until successful login')
def test_log_in_twitter(driver):
    login = L.LoginPage(driver)
    common = L.Commons(driver)
    with allure.step('Going to the log - in area'):
        common.click_login_signup()
    with allure.step('Trying to log in with twitter'):
        login.click_twitter_login()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://twitter.com/'
        # CAN'T CONTINUE TEST -- TWITTER CONNECTION IS FAILING


@allure.epic('Test Login')
@allure.id(16)
@allure.title('Log in with Google account')
@allure.description('The Google login page will show up - redirecting through 3rd party until successful login')
def test_log_in_google(driver):
    login = L.LoginPage(driver)
    common = L.Commons(driver)
    with allure.step('Going to the log - in area'):
        common.click_login_signup()
    with allure.step('Trying to log in with google'):
        login.click_google_login()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://accounts.google.com/signin/oauth/success'
        # CAN'T CONTINUE TEST -- GOOGLE CONNECTION IS FAILING


@allure.epic('Test Login')
@allure.id(58)
@allure.title('Log in with facebook account')
@allure.description('The Facebook login page will show up - redirecting through 3rd party until successful login')
def test_log_in_facebook(driver):
    login = L.LoginPage(driver)
    common = L.Commons(driver)
    with allure.step('Going to the log - in area'):
        common.click_login_signup()
    with allure.step('Trying to log in with facebook'):
        login.click_facebook_login()
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://www.facebook.com/login.php?skip_api_login=1'
        # CAN'T CONTINUE TEST -- FACEBOOK CONNECTION IS FAILING


@allure.epic('Test Login')
@allure.id(17)
@allure.title('Remember me functionality')
@allure.description('The remember me button wil save the entered user for future logins')
def test_remember_me(driver):
    login = L.LoginPage(driver)
    common = L.Commons(driver)
    with allure.step('Logging in with remember me'):
        login.log_in('0000000000', True, False)
    with allure.step('Logging out and going back to login page'):
        common.click_logout()
        common.click_login_signup()
    with allure.step('Asserting phone number was remembered'):
        txt = login.assert_remember_me_worked()
        assert txt == '0000000000'

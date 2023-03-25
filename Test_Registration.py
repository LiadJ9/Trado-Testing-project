import pytest
import Project_folder.pages.Registration_pages as Rp
import Project_folder.pages.common_page as C
import Project_folder.MongoDB_requests as R
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Registration')
@allure.id(18)
# @allure.story("Creating a new account and validating it with a security code")
@allure.title("Register valid account - security valid")
@allure.description('The intended way to create a new account')
@allure.severity(allure.severity_level.CRITICAL)
def test_sign_up_with_valid_info(driver):
    signup = Rp.SignupPage(driver)
    common = C.Commons(driver)
    with allure.step('Creating the valid account with both preferences'):
        phone_number = signup.sign_up(True, True, True, True, True, True, False)
    with allure.step('Navigating to the user page area'):
        common.click_login_signup()

    with allure.step("Asserting that the current url is the personal area url -- can only be accessed once you are logged in"):
        assert driver.current_url == 'https://qa.trado.co.il/user/personalArea'
    with allure.step("Asserting that the user exists in the DB"):
        request = R.MongoRequests()
        request.assert_user_exists(phone_number)


@allure.epic('Test Registration')
@allure.id(19)
@allure.title('Register valid account - security invalid')
@allure.description("Making sure accounts can't be accessed with no valid security code")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_sign_up_with_existing_account_security_invalid(driver):
    signup = Rp.SignupPage(driver)
    with allure.step('Creating a valid account with an invalid security number'):
        signup.sign_up(True, True, False, True, True, True, False)


@allure.epic('Test Registration')
@allure.id(20)
@allure.title('Register account - invalid phone number - Valid business number - (N) - PP true')
@allure.description('Registering an account wih invalid phone number + valid business number should deny access')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_signup_invalid_phone_number_and_valid_business_num(driver):
    signup = Rp.SignupPage(driver)
    with allure.step('Creating an invalid account'):
        signup.sign_up(True, True, True, True, True, False, False)


@allure.epic('Test Registration')
@allure.id(21)
@allure.title('Register account - invalid phone number - Invalid business number - (N) PP true')
@allure.description('Registering an account with an invalid phone number + invalid business number should deny access')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_signup_invalid_phone_invalid_business_num(driver):
    signup = Rp.SignupPage(driver)
    with allure.step('Creating an invalid account'):
        signup.sign_up(True, True, True, False, True, False, False)


@allure.epic('Test Registration')
@allure.id(22)
@allure.title('Register account - valid phone number - invalid business number - (N) PP true')
@allure.description('Registering an account with an invalid business number (such as a special letter) should show a respective error')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_signup_valid_phone_invalid_phone_number(driver):
    signup = Rp.SignupPage(driver)
    with allure.step('Creating an invalid account'):
        signup.sign_up(True, True, True, False, True, True, False)


@allure.epic('Test Registration')
@allure.id(23)
@allure.title('Register valid account - PP(Privacy policy) False (N)')
@allure.description('Registering a valid account without accepting the privacy policy should show an alert')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_signup_valid_phone_no_privacy(driver):
    signup = Rp.SignupPage(driver)
    with allure.step('Creating valid account with no privacy policy'):
        signup.sign_up(True, True, True, True, False, True, False)


@allure.epic('Test Registration')
@allure.id(24)
@allure.title('Ensure Mailing list functionality')
@allure.description('Checking that marking the mailing list option will actually add the user to the mailing list in the database')
@allure.severity(allure.severity_level.NORMAL)
def test_signup_mailing_list(driver):
    signup = Rp.SignupPage(driver)
    requests = R.MongoRequests()
    with allure.step('Creating a valid account with mailing list'):
        phone_num, security_code = signup.sign_up(True, True, True, True, True, True, True)
    with allure.step("Making sure the new account's mail list status is True"):
        mailing_list = requests.get_mailing_list_status(phone_num)
        assert mailing_list



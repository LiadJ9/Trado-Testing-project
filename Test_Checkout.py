import random

import pytest
import Project_folder.pages.Login_Pages as L
import Project_folder.pages.Checkout_page as C
import Project_folder.pages.Product_pages as P
import Project_folder.pages.Registration_pages as R
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Checkout')
@allure.id(55)
@allure.title("Continue with order btn")
@allure.description('Verify Continue with order button returns you to main page')
@allure.severity(allure.severity_level.MINOR)
def test_click_continue_with_order(driver):
    products = P.ProductPage(driver)
    login = L.LoginPage(driver)
    checkout = C.CheckoutPage(driver)
    with allure.step('Logging in'):
        login.log_in('0000000000', False, False)
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('clicking checkout'):
        checkout.click_checkout()
    with allure.step('clicking continue with order button'):
        checkout.click_continue_order()
    with allure.step('asserting the right location'):
        assert driver.current_url == 'https://qa.trado.co.il/'


@allure.epic('Test Checkout')
@allure.id(56)
@allure.title("Ordering with valid details")
@allure.description('An order will be placed under the current user')
@allure.severity(allure.severity_level.CRITICAL)
def test_order_valid_details(driver):
    products = P.ProductPage(driver)
    signup = R.SignupPage(driver)
    checkout = C.CheckoutPage(driver)
    login = L.LoginPage(driver)
    # with allure.step('Signing up'):
    #     phone_number, code = signup.sign_up(True, True, True, True, True, True, False)
    #     print(phone_number)
    login.log_in('0000000000', True, False)
    with allure.step('Going to store page'):
        driver.get('https://qa.trado.co.il/')
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('clicking checkout'):
        checkout.click_checkout()
    with allure.step('Filling out order form -- if needed'):
        checkout.click_already_filled_form()
        # checkout.fill_out_form(f'{signup.random_usr_name()}', '9', 'Goober@bmail.com', 'Joshualane', 'telaviv', 8, 2, 3, 'baruch simple', 'baruch', 'advanced')
        checkout.go_to_credit_card_page()
        driver.switch_to.frame(checkout.find_frame())
    with allure.step('Adding credit card'):
        checkout.add_credit_card()
    with allure.step('Asserting order confirmation'):
        checkout.assert_order_confirmed()


@allure.epic('Test Checkout')
@allure.id(57)
@allure.title("Ordering with invalid details")
@allure.description('A respective error message will show up')
@allure.severity(allure.severity_level.CRITICAL)
def test_order_invalid_details(driver):
    products = P.ProductPage(driver)
    signup = R.SignupPage(driver)
    checkout = C.CheckoutPage(driver)
    login = L.LoginPage(driver)
    login.log_in('2222222222', True, False)
    with allure.step('Going to store page'):
        driver.get('https://qa.trado.co.il/')
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('clicking checkout'):
        checkout.click_checkout()
    with allure.step('Filling out order form -- if needed'):
        checkout.fill_out_form(f'{signup.random_usr_name()}', '-1', '1@!1111wkrq', 'Joshu9iiokje', 'telav908iv', 8999, 2, 3, 'baru9ch simple', 'b9aruch', 'advan@ced')
    with allure.step('Asserting error message'):
        checkout.assert_invalid_details_message()


@allure.epic('Test Checkout')
@allure.id(29)
@allure.title("Ordering an amount of random higher that is higher than it's stock (N)")
@allure.description('Ordering more of an item than actual stock available should show a respective error')
@allure.severity(allure.severity_level.CRITICAL)
def test_high_item_count(driver):
    checkout = C.CheckoutPage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging up'):
        login.log_in('0000000000', True, False)
    with allure.step('Going to product'):
        driver.get('https://qa.trado.co.il/product/04991')
    with allure.step('Adding the random product'):
        checkout.order_2000_items()
    with allure.step('clicking checkout'):
        checkout.click_checkout()
    with allure.step('Filling out order form -- if needed'):
        checkout.click_already_filled_form()
        checkout.go_to_credit_card_page()
        driver.switch_to.frame(checkout.find_frame())
    with allure.step('Adding credit card'):
        checkout.add_credit_card()
    with allure.step('Asserting order failure'):
        # ASSERT ORDER FAILED PLACEHOLDER - NOT AVAILABLE
        pass


@allure.epic('Test Checkout')
@allure.id(30)
@allure.title("Ordering with no credit card info (N)")
@allure.description('Trying to order with no credit card info should show a respective error')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.xfail(condition=lambda: True, reason='EXPECTED LOGIN FAILURE')
def test_no_credit_card(driver):
    checkout = C.CheckoutPage(driver)
    login = L.LoginPage(driver)
    with allure.step('Logging up'):
        login.log_in('0000000000', True, False)
    with allure.step('Going to product'):
        driver.get('https://qa.trado.co.il/product/04991')
    with allure.step('Adding the random product'):
        checkout.order_2000_items()
    with allure.step('clicking checkout'):
        checkout.click_checkout()
    with allure.step('Filling out order form -- if needed'):
        checkout.click_already_filled_form()
        checkout.go_to_credit_card_page()
        checkout.place_order()
    with allure.step('Asserting order confirmation'):
        checkout.assert_order_confirmed()


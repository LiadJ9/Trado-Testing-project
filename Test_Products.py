import pytest
import Project_folder.pages.Product_pages as P
import Project_folder.MongoDB_requests as R
import allure


@pytest.fixture
def selection():
    # F -- FIREFOX C -- CHROME E -- EDGE
    return 'F'


@allure.epic('Test Products')
@allure.id(25)
@allure.title("Random product added to cart")
@allure.description('Check that the random product is actually added to user cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_item_to_cart(driver):
    products = P.ProductPage(driver)
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('Asserting item has been added to cart'):
        size = products.get_cart_list_size()
        assert size == 1


@allure.epic('Test Products')
@allure.id(26)
@allure.title("Random product display details same as DB")
@allure.description('Check that product information between site and DB is accurate')
@allure.severity(allure.severity_level.NORMAL)
def test_random_item_details(driver):
    products = P.ProductPage(driver)
    request = R.MongoRequests()
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Getting Necessary information about the random product'):
        id = products.get_number(products.PRODUCT_ID)
        units_per = products.get_number(products.UNITS_PER_CARTON)
        price_per = products.get_decimal_number(products.PRICE_PER_CARTON)
        stock = products.get_number(products.STOCK_AMOUNT)
        dbstock, dbprice, dbunits_in_carton = request.get_product_info(str(id))
    with allure.step('Verifying in the database that the info is correct'):
        assert dbprice == price_per
        assert units_per == dbunits_in_carton
        assert stock == dbstock


@allure.epic('Test Products')
@allure.id(27)
@allure.title('Verify "Empty cart" Button functionality')
@allure.description('Verify that the empty cart button removes all items from cart')
@allure.severity(allure.severity_level.MINOR)
def test_clear_cart(driver):
    products = P.ProductPage(driver)
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('Clearing the cart'):
        products.clear_cart()
    with allure.step('Asserting cart is empty'):
        size = products.get_cart_list_size()
        assert size == 0


@allure.epic('Test Products')
@allure.id(28)
@allure.title('Dynamic cart in /products page updates as items are added')
@allure.description('Verify that the dynamic cart element updates as items in the cart change')
@allure.severity(allure.severity_level.NORMAL)
def test_dynamic_cart(driver):
    products = P.ProductPage(driver)
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('Getting Necessary information about the random product in cart'):
        cartons_before = products.get_number(products.CARTONS_IN_CART)
        units_before = products.get_number(products.UNITS_IN_CART)
        price_before = products.get_decimal_number(products.CART_ITEM_PRICE)
    with allure.step('Adding additional item to cart'):
        products.click_(products.ADD_PRODUCT_IN_CART)
    with allure.step('Asserting price, units and cartons have changed'):
        assert units_before != products.get_number(products.UNITS_IN_CART)
        assert cartons_before+cartons_before == products.get_number(products.CARTONS_IN_CART)
        assert price_before+price_before == products.get_number(products.CART_ITEM_PRICE)


@allure.epic('Test Products')
@allure.id(31)
@allure.title('Verify the information displayed in the cart section')
@allure.description('Comparing the items in the cart and ensure the final total shows correct information ')
@allure.severity(allure.severity_level.CRITICAL)
def test_cart_summary(driver):
    products = P.ProductPage(driver)
    with allure.step('selecting random product'):
        products.select_random_product()
    with allure.step('Adding the random product'):
        products.click_(products.ADD_PRODUCT)
    with allure.step('Getting Necessary information about the random product in cart'):
        price_of_item = products.get_decimal_number(products.CART_ITEM_PRICE)
        pre_tax_sum = products.get_decimal_number(products.SUM_BEFORE_TAX)
        tax_addition = products.get_decimal_number(products.TAX_RATE)
        tax_sum = products.get_decimal_number(products.SUM_AFTER_TAX)
    with allure.step('Asserting information is correct'):
        assert price_of_item == pre_tax_sum
        assert price_of_item+tax_addition == tax_sum









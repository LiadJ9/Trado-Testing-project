from Project_folder.pages.Utils.TRADO_UTILS import pytest
import Project_folder.pages.Utils.TRADO_UTILS as U
from Project_folder.pages.common_page import Commons


@pytest.fixture
def driver(selection):
    url = 'https://qa.trado.co.il/'
    if selection == 'F':
        driver = U.Firefox()
    elif selection == 'C':
        driver = U.Chrome()
    elif selection == 'E':
        driver = U.Edge()
    else:
        print('invalid selection ---- selecting default:: Firefox')
        driver = U.Firefox()
    driver.get(url)
    if U.wdw(driver, 10).until(U.ec.visibility_of_element_located(Commons.STORE_WELCOME)):
        driver.find_element(*Commons.STORE_WELCOME_DISMISS).click()
    yield driver
    driver.close()

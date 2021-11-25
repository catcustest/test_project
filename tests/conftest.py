import pytest
from selene.browser import set_driver, quit_driver, open_url, driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from elements.pages.kicherchekoi.kicherchekoi_home_page import KicherchekoiHomePage
from elements.pages.trainline.trainline_home_page import TrainlineHomePage, TrainlineSearchResultPage
from elements.pages.xkcd.xkcd_home_page import HomePage
from elements.utils import get_config

XKCD_URL = get_config()["sites"]["xkcd"]["base_api_url"]
KICHERCHEKOI_URL = get_config()["sites"]["kicherchekoi"]["base_api_url"]
TRAINLINE_URL = get_config()["sites"]["trainline"]["base_api_url"]


@pytest.fixture
def xkcd_home_page():
    set_driver(webdriver.Chrome(ChromeDriverManager().install()))
    open_url(XKCD_URL)
    home_page = HomePage()
    yield home_page
    quit_driver()


@pytest.fixture
def kicherchekoi_home_page():
    set_driver(webdriver.Chrome(ChromeDriverManager().install()))
    open_url(KICHERCHEKOI_URL)
    home_page = KicherchekoiHomePage()
    yield home_page
    quit_driver()


@pytest.fixture
def trainline_home_page(browser):
    home_page = TrainlineHomePage()
    return home_page


@pytest.fixture
def trainline_train_details_page(browser):
    result_page = TrainlineSearchResultPage()
    return result_page


@pytest.fixture
def browser():
    set_driver(webdriver.Chrome(ChromeDriverManager().install()))
    open_url(TRAINLINE_URL)
    yield driver()
    quit_driver()

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from application.application import Application


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def browser_name(request):
    return request.config.getoption("--browser_name")


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app

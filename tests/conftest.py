from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose a browser to run the test(s): chrome or firefox",
    )


@fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == "chrome":
        chrome_service_obj = Service("./resources/webdrivers/chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=chrome_service_obj, options=chrome_options)
    elif browser_name == "firefox":
        ff_service_obj = Service("./resources/webdrivers/geckodriver.exe")
        driver = webdriver.Firefox(service=ff_service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)  # 5 seconds is max timeout: 2 seconds (3 seconds save)

    request.cls.driver = driver

    yield

    driver.close()

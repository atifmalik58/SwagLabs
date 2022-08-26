""" pytest configurations """
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True)
def setup(request, url, browser, ver):
    """
    SetUp & TearDown fixture for pytest
    """
    global driver
    """ browser name and version selection based on cmd line arguments """
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(path=r".\\drivers", version=ver).install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager(path=r".\\drivers", version=ver).install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager(path=r".\\drivers", version=ver).install()))
    else:
        print("Choose the correct browser")

    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()


def pytest_addoption(parser):
    """ adds custom cmd line arguments """
    parser.addoption("--url",
                     help="Application URL on which testing is to be performed",
                     default="https://www.saucedemo.com/")
    parser.addoption("--browser",
                     help="Browser on which testing is to be performed; valid inputs firefox, chrome, edge")
    parser.addoption("--ver",
                     help="Driver version for testing; Note: incorrect version would result in execution failure")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    """ gets URL value from cmd line arguments """
    return request.config.getoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    """ gets Browser name from cmd line arguments """
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def ver(request):
    """ gets browser version from cmd line arguments """
    return request.config.getoption("--ver")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """ Sets Test Report destination folder """
    if not os.path.exists('reports'):
        os.makedirs('reports')
    config.option.htmlpath = 'reports/' + "report_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"


def pytest_html_report_title(report):
    """ Sets Test Report Title """
    report.title = "SwagLabs Verification Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Creates Test Report and Embed Screenshots for Failed Test cases """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            if not os.path.exists('reports/screenshots'):
                os.makedirs('reports/screenshots')
            screenshots_dir = os.path.dirname(r'.\\reports\\screenshots\\')
            screenshot_name = "screenshot_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".png"
            screenshot_destination = os.path.join(screenshots_dir, screenshot_name)
            driver.save_screenshot(screenshot_destination)
            if screenshot_name:
                html = f'<div><img src="screenshots/{screenshot_name}" alt="screenshot" ' \
                       f'style="width:304px;height:228px;"onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

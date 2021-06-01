import logging
import pytest
import os

from common.utils import create_browser, get_browser_name

logger = logging.getLogger(__name__)

BASE_URL = {
    "prod" : "https://www.fylehq.com",
    "stag1" : "https://staging1.fyle.tech",
    "stag2" : "https://staging2.fyle.tech",
    "local" : "http://localhost:4000"
}

#Parser adoption to use custom arguments from command line
def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="prod")

@pytest.fixture(scope='session')
def url(request):
    base_url = request.config.option.url
    if base_url is None:
        pytest.skip()
    return base_url


@pytest.fixture(scope='module')
def base_url(url):
    return BASE_URL[url]

#Assigning capabilities based on where the test case is going to run.(Remote or Local)
BROWSER_CAPABALITIES = [None] if get_browser_name() != 'remote' else [
        {
            "build" : "Multi config test",
            "name" : "Bad email - windows",
            "platform" : "Windows 10",
            "browserName" : "Chrome",
            "version" : "88.0",
        },

        {
            "build" : "Multi config test",
            "name" : "Bad email - mac",
            "platform" : "MacOS Big sur",
            "browserName" : "Safari",
            "version" : "14.0",
        },

        {
            "build" : "Test build",
            "name" : "Bad email - firefox",
            "platform" : "Windows 10",
            "browserName" : "Firefox",
            "version" : "87.0"
        },

        {
            "build" : "Test build",
            "name" : "Bad emial - IE",
            "platform" : "Windows 10",
            "browserName" : "Internet Explorer",
            "version" : "11.0",
            "ie.compatibility" : 11001
        }
    ]

#Assigning parameter to this fixture, allowing all the test cases to run on number of browser capabilites
@pytest.fixture(params=BROWSER_CAPABALITIES, scope='module')
def module_browser(base_url, request):
    browser_name = get_browser_name()
    browser = create_browser(browser_name, request.param)
    browser.get(base_url)
    browser.click(xpath="//span[contains(@class, 'banner-close')]")
    yield browser
    browser.quit()

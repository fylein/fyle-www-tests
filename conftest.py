import time
import logging
import pytest

from common.utils import create_browser, resize_browser, get_browser_name

logger = logging.getLogger(__name__)

@pytest.fixture(scope='module')
def base_url():
    return 'https://ww2.fylehq.com'

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
    browser.close()

#Setting the resolution parameters in fixture itself, this avoids adding @mark.parameterize() for every test cases.
@pytest.fixture(params=[('desktop_1'), ('mobile_1')], scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/')
    time.sleep(4)
    return module_browser

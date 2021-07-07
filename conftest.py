import logging
import pathlib
import pytest
import datetime
import pytz

from common.utils import create_browser, get_browser_name

logger = logging.getLogger(__name__)

BASE_URL = {
    "prod" : "https://www.fylehq.com",
    "stag1" : "https://staging1.fyle.tech",
    "stag2" : "https://staging2.fyle.tech",
    "local" : "http://localhost:4000"
}

zone = pytz.timezone('Asia/Kolkata')
current_time = datetime.datetime.now(zone).strftime("%d-%m-%Y, %I:%M:%S %p")
test_name = f"Test on: {current_time}"

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
        "build" : test_name,
        "name" : test_name,
        "platform" : "Windows 10",
        "browserName" : "Chrome",
        "version" : "88.0",
        "console" : True,
		"network" : True
    }
]

BROWSER_CAPABALITIES_MOBILE = [None] if get_browser_name() != 'remote' else [
    {
        "build" : test_name,
        "name" : test_name,
        "platform" : "Windows 10",
        "browserName" : "Chrome",
        "version" : "88.0",
        "console" : True,
		"network" : True
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

@pytest.fixture(params=BROWSER_CAPABALITIES_MOBILE, scope='module')
def module_browser_mobile(base_url, request):
    browser_name = get_browser_name()
    browser = create_browser(browser_name, request.param)
    browser.get(base_url)
    browser.click(xpath="//span[contains(@class, 'banner-close')]")
    yield browser
    browser.quit()

def pytest_collection_modifyitems(config, items):
    rootdir = pathlib.Path(config.rootdir)
    for item in items:
        rel_path = pathlib.Path(item.fspath).relative_to(rootdir)
        for part in rel_path.parts:
            mark_name = part.split('_')[-1].split('.')[0]
        if mark_name in ['mobile', 'laptop']:
            mark = getattr(pytest.mark, mark_name)
            item.add_marker(mark)
        else:
            mark = getattr(pytest.mark, 'desktop')
            item.add_marker(mark)
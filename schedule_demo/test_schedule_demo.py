import time
import logging
import pytest

from common.asserts import assert_overflowing
from common.utils import resize_browser
from common.inline_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/schedule-demo')
    time.sleep(4)
    return module_browser

#Check demo form (common section)
@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_bad_email(browser):
    assert_bad_email(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_required_fields(browser):
    assert_required_fields(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_non_business_email(browser):
    assert_non_business_email(browser=browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_invalid_names(browser):
    assert_invalid_names(browser=browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_success(browser):
    assert_success(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_page_overflow(browser):
    assert_overflowing(browser=browser)

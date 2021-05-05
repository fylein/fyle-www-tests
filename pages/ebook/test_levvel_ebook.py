from time import sleep
import logging
import pytest
from common.utils import resize_browser
from common.asserts import assert_typography, assert_overflowing
from common.content_download_form import assert_content_download_inline_form, assert_required_fields, assert_invalid_names, assert_bad_email, assert_non_business_email, assert_success_download_form

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    sleep(4)
    module_browser.get(base_url + '/resources/ebooks/levvel-t&e-report')
    sleep(2)
    return module_browser

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_page_overflow(browser):
    assert_overflowing(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_typography(browser):
    assert_typography(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_content_download_inline_form(browser):
    assert_content_download_inline_form(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_required_fields(browser):
    assert_required_fields(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_invalid_names(browser):
    assert_invalid_names(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_bad_email(browser):
    assert_bad_email(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_non_business_email(browser):
    assert_non_business_email(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_success_download_form(browser):
    assert_success_download_form(browser, 'Travel & Expense Management Report by Levvel Research', 'test@fyle.in', 'https://cdn2.hubspot.net/hubfs/3906991/Paystream%202018%20Travel%20and%20Expense%20Management%20report.pdf')

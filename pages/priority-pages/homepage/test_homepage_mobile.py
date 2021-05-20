import logging

from common.asserts import assert_overflowing
from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names
from common.components.resources import assert_resources_section
from common.components.sneak_peek import assert_sneak_peek_section

from homepage import mobile_browser as browser


logger = logging.getLogger(__name__)

#Check demo form (common section)
def test_bad_email(browser):
    assert_bad_email(browser)

def test_required_fields(browser):
    assert_required_fields(browser)

def test_non_business_email(browser):
    assert_non_business_email(browser)

def test_invalid_names(browser):
    assert_invalid_names(browser)

def test_success(browser):
    assert_success(browser)

def test_resources_section(browser, base_url):
    links = ['/resources/expense-management-roi-calculator', '/resources/ebooks/automate-travel-expense-management', '/resources']
    assert_resources_section(browser, base_url, links)

def test_page_overflow(browser):
    assert_overflowing(browser=browser)

def test_sneak_peek_section(browser):
    assert_sneak_peek_section(browser)

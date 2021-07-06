from common.asserts import assert_overflowing
from common.components.demo_form import *
from .common.schedule_demo import *

from . import mobile_browser as browser

def test_bad_email(browser):
    assert_bad_email(browser, inline=True)

def test_required_fields(browser):
    assert_required_fields(browser, inline=True)

def test_non_business_email(browser):
    assert_non_business_email(browser=browser, inline=True)

def test_invalid_names(browser):
    assert_invalid_names(browser=browser, inline=True)

def test_success(browser):
    assert_success(browser, inline=True)

def test_page_overflow(browser):
    assert_overflowing(browser=browser)

def test_demo_section(browser):
    assert_demo_section(browser, 10, 21)

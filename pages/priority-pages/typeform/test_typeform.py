import logging
from common.components.typeform import *
from . import desktop_browser as browser

logger = logging.getLogger(__name__)

def test_typeform_open(browser):
    open_typeform(browser)

def test_typeform_close(browser):
    close_typeform(browser)

def test_email_validation(browser):
    assert_invalid_email(browser)

def test_required_fields(browser):
    assert_required_fields(browser)

def test_phone_number_validation(browser):
    assert_invalid_phone_number(browser)

def test_form_success(browser):
    assert_form_success(browser)

def test_form_success_with_keys(browser):
    assert_form_success(browser, keys=True)

def test_name_validation(browser):
    assert_invalid_names(browser)

def test_thank_you_gif(browser):
    assert_thank_you_gif(browser)

def test_logo_image(browser):
    assert_logo(browser)

def test_tc_url(browser, base_url):
    assert_tc_url(browser, base_url)

def test_upward_arrow(browser):
    assert_upward_arrow(browser)

def test_downward_arrow(browser):
    assert_downward_arrow(browser)

def test_values_after_closing_form(browser):
    assert_values_after_closing_form(browser)

def test_thankyou_page_urls(browser, base_url):
    assert_thankyou_page_urls(browser, base_url)

# def test_goto_missing_fields(browser):
#     assert_goto_missing_fields(browser, firstname='test', lastname='test', phone='345689763', size='>1000')

# def test_progress_bar(browser):
#     assert_progress_bar(browser)

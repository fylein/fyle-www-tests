import logging
from common.components.steps_form import *
from . import desktop_browser as browser

logger = logging.getLogger(__name__)

def test_steps_form_open(browser):
    open_steps_form(browser)

def test_steps_form_close(browser):
    close_steps_form(browser)

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

def test_logo_image(browser):
    assert_logo(browser)

def test_terms_and_conditions_url(browser, base_url):
    assert_terms_and_conditions_url(browser, base_url)

def test_navigation(browser):
    assert_navigation(browser)

def test_values_after_closing_form(browser):
    assert_values_after_closing_form(browser)

def test_thankyou_page_urls(browser, base_url):
    assert_thankyou_page_urls(browser, base_url)

def test_goto_missing_fields(browser):
    assert_goto_missing_fields(browser)

def test_firstname_in_phone_field(browser):
    assert_firstname_in_phone_field(browser)

def test_progress_bar(browser):
    assert_progress_bar(browser)

def test_form_width(browser):
    assert_form_width(browser)

def test_field_spacing(browser):
    assert_field_spacing(browser)

def test_radio_pill_spacing(browser):
    assert_radio_pill_spacing(browser)

def test_gdpr_checkbox(browser):
    assert_gdpr_checkbox(browser)

import logging
from common.components.typeform import *
from . import mobile_browser as browser

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
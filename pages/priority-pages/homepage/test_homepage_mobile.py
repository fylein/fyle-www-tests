import time
import logging
import pytest

from . import mobile_browser as browser
from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_links
from common.utils import resize_browser
from common.components.para_blocks import assert_para_blocks
from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names
from common.components.resources import assert_resources_section
from common.components.sneak_peek import assert_sneak_peek_section

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

# def test_success(browser):
#     assert_success(browser)

# def test_page_overflow(browser):
#     assert_overflowing(browser=browser)

# def test_para_block(browser):
#     assert_para_blocks()

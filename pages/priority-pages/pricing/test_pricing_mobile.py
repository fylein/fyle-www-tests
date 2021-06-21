import logging
import time

from common.asserts import assert_overflowing, assert_spacing, assert_dimensions, assert_overlap
from common.components.steps_form import assert_steps_form_modal, close_steps_form
from common.components.pricing import *

from . import mobile_browser as browser

logger = logging.getLogger(__name__)

def test_annual_price(browser):
    assert_annual_price(browser)

def test_monthly_price(browser):
    assert_monthly_price(browser)

def test_toggling(browser):
    assert_toggling(browser)

def test_see_details(browser):
    assert_see_details(browser)

def test_usage_led_pricing(browser):
    assert_usage_led_pricing(browser, 411, 80)

def test_comparison_section(browser):
    assert_comparison_section(browser)

def test_sticky_header(browser):
    assert_sticky_header(browser, top_value=62)

def test_faq_spacing(browser):
    assert_faq_spacing(browser, 40, 20)

def test_faq_card_spacing(browser):
    assert_faq_card_spacing(browser, 20)
    #Assert bottom spacing
    columns = browser.find_many('//section[contains(@class, "faq")]//div[contains(@class, "row") and contains(@class, "stretch")]//div[contains(@class, "col")]')
    for i, col in enumerate(columns):
        if i != 2 and i != 4:
            assert_spacing('bottom', col, 20)
        else:
            assert_spacing('bottom', col, 0)

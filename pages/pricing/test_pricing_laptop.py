import logging

from common.asserts import assert_overflowing, assert_spacing
from common.components.pricing import *

from . import laptop_browser as browser

logger = logging.getLogger(__name__)

def test_annual_price(browser):
    assert_annual_price(browser)

def test_monthly_price(browser):
    assert_monthly_price(browser)

def test_toggling(browser):
    assert_toggling(browser)

def test_demo_form_buttons(browser):
    assert_demo_form_buttons(browser)

def test_card_spacing(browser):
    cards = browser.find_many('//div[contains(@class, "card-group")]//div[contains(@class, "card ")]')
    for i, card in enumerate(cards):
        if i != 1:
            assert_spacing('left', card, 0)
            assert_spacing('right', card, 0)
        else:
            assert_spacing('left', card, 13)
            assert_spacing('right', card, 13)

def test_card_width(browser):
    assert_card_width(browser, 366, 1200, 1234)

def test_title_desc_width(browser):
    assert_title_desc_width(browser, 306, 60)

def test_feature_list(browser):
    assert_feature_list(browser, 282)

def test_usage_led_pricing(browser):
    assert_usage_led_pricing(browser, 984, 40)

def test_comparison_section(browser):
    assert_comparison_section(browser)

def test_scroll_btn(browser):
    assert_scroll_btn(browser)

def test_comparison_demo_button(browser):
    assert_comparison_demo_button(browser)

def test_sticky_header(browser):
    assert_sticky_header(browser)

def test_faq_spacing(browser):
    assert_faq_spacing(browser, 100, 40)

def test_faq_card_spacing(browser):
    assert_faq_card_spacing(browser, 40, 40)

def test_page_overflow(browser):
    assert_overflowing(browser)

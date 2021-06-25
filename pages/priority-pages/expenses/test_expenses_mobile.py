from common.components.slider import *
from common.components.hero import assert_product_mobile_hero_section
from common.asserts import assert_overflowing
from common.components.sneak_peek import *

from . import mobile_browser as browser

def test_hero_section(browser):
    assert_product_mobile_hero_section(browser, 354)

def test_sneak_peek_section(browser):
    assert_sneak_peek_section(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

from common.components.para_blocks import *
from common.components.hero import assert_product_hero_section
from common.asserts import *

from . import laptop_browser as browser

def test_hero_section(browser):
    assert_product_hero_section(browser, 1140, 997)

def test_para_block(browser):
    assert_para_blocks(browser, para_width=518, image_width=622, spacing=60)
    assert_para_block_section_spacing(browser, spacing=100)

def test_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def test_page_overflow(browser):
    assert_overflowing(browser)
from common.components.para_blocks import *
from common.components.hero import assert_product_mobile_hero_section
from common.asserts import *

from . import mobile_browser as browser

def test_hero_section(browser):
    assert_product_mobile_hero_section(browser, 354)

def test_para_block(browser):
    assert_para_blocks(browser, para_width=440, image_width=440)
    assert_para_block_section_spacing(browser, spacing=40)

def test_page_overflow(browser):
    assert_overflowing(browser)

from common.asserts import *
from common.components.para_blocks import *
from common.components.hero_v2 import assert_hero_v2_section

from . import mobile_browser as browser

def test_hero_section(browser):
    assert_hero_v2_section(browser, 'capterra-hero', bulletin=False)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=440, image_width=440)

def test_page_overflow(browser):
    assert_overflowing(browser)

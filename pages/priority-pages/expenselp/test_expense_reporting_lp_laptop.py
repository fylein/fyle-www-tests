from common.asserts import *
from common.components.para_blocks import *
from common.components.hero_v2 import assert_hero_v2_section

from . import laptop_browser as browser

def test_hero_section(browser):
    assert_hero_v2_section(browser, 'capterra-hero', img_width=728, logo_width=997, bulletin=False)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=518, image_width=622, spacing=60)

def test_bottom_banner_cta(browser):
    assert_bottom_banner_cta(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

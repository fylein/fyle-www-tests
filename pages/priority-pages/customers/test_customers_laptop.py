import logging

from common.asserts import assert_overflowing, assert_fyle_over_expensify_img_section, assert_bottom_banner_cta
from common.components.hero import assert_h1_spacing, assert_subtext_spacing, assert_img
from common.components.para_blocks import *

from . import laptop_browser as browser

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class = 'fyle-design-system'
    assert_h1_spacing(browser, section_class)
    assert_subtext_spacing(browser, section_class)
    assert_img(browser, 690, section_class)

def test_fyle_over_expensify_img_section(browser):
    assert_fyle_over_expensify_img_section(browser, width=1140, height=286)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=518, image_width=622, spacing=60)

def test_bottom_banner_cta(browser):
    assert_bottom_banner_cta(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

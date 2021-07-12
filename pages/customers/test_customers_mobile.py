import logging

from common.asserts import assert_overflowing
from common.components.hero import assert_h1_spacing, assert_subtext_spacing
from common.components.para_blocks import *

from . import mobile_browser as browser

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class = 'fyle-design-system'
    assert_h1_spacing(browser, section_class, 16)
    assert_subtext_spacing(browser, section_class, 0)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=440, image_width=440)

def test_page_overflow(browser):
    assert_overflowing(browser)

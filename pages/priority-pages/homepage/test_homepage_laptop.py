import logging

from common.asserts import assert_overflowing
from common.components.para_blocks import assert_para_blocks
from common.components.sneak_peek import assert_sneak_peek_section

from . import laptop_browser as browser



logger = logging.getLogger(__name__)


def test_page_overflow(browser):
    assert_overflowing(browser)

def test_para_blocks(browser):
    assert_para_blocks(browser, para_width=505, image_width=635, spacing=60)

def test_sneak_peek_section(browser):
    assert_sneak_peek_section(browser, text_width=487, img_width=682)

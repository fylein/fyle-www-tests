import logging

from common.asserts import assert_overflowing
from common.components.hero import assert_hero_section
from common.components.para_blocks import assert_para_blocks
from common.asserts import verify_url_by_link_text
# from common.components.navbar import assert_navbar
# from common.components.footer import assert_footer

from . import laptop_browser as browser

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class = 'homepage-hero'
    assert_hero_section(browser, section_class, 1140, 1140)

def test_para_blocks(browser, base_url):
    assert_para_blocks(browser, para_width=505, image_width=635, spacing=60)
    verify_url_by_link_text(browser, 'Turn expense reporting real-time', base_url, '/product/expenses')
    verify_url_by_link_text(browser, 'Automate corporate card reconciliations', base_url, '/product/cards')
    verify_url_by_link_text(browser, 'Check out how data flows in and out of Fyle', base_url, '/product/integrations')
    verify_url_by_link_text(browser, 'More informed decisions with all the expense', base_url, '/product/analytics')

def test_page_overflow(browser):
    assert_overflowing(browser)

# def test_sneak_peek_section(browser):
#     assert_sneak_peek_section(browser, text_width=487, img_width=682)

import logging

from common.asserts import assert_overflowing
from common.components.navbar import assert_mobile_navbar
from common.components.footer import assert_footer
from common.components.hero import assert_mobile_hero_section
from common.asserts import verify_url_by_link_text
from common.components.para_blocks import *


from . import mobile_browser as browser

logger = logging.getLogger(__name__)

# def test_hero_section(browser):
#     section_class = 'homepage-hero'
#     assert_mobile_hero_section(browser, section_class)

# def test_para_block_spacing(browser):
#     assert_para_blocks(browser, para_width=440, image_width=440)
#     assert_para_block_section_spacing(browser, spacing=40)

# def test_para_block_links(browser, base_url):
#     verify_url_by_link_text(browser, 'Turn expense reporting real-time', base_url, '/product/expenses')
#     verify_url_by_link_text(browser, 'Automate corporate card reconciliations', base_url, '/product/cards')
#     verify_url_by_link_text(browser, 'Check out how data flows in and out of Fyle', base_url, '/product/integrations')
#     verify_url_by_link_text(browser, 'More informed decisions with all the expense', base_url, '/product/analytics')

# def test_navbar(browser, base_url):
#     assert_mobile_navbar(browser, base_url)

# def test_footer(browser, base_url):
#     assert_footer(browser, base_url)

def test_page_overflow(browser):
    assert_overflowing(browser)

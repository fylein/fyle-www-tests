import logging

from common.asserts import assert_overflowing
from common.components.hero import *
from common.components.para_blocks import *
from common.asserts import verify_url_by_link_text

from . import laptop_browser as browser

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class = 'homepage-hero'
    assert_h1_spacing(browser, section_class)
    assert_subtext_spacing(browser, section_class)
    assert_img(browser, 1140, section_class)
    assert_button_spacing(browser, section_class)
    assert_customer_logo(browser, 1140,
        section_xpath=f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section',
        logo_xpath=f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//img[contains(@class, "hero-customer-logo")]',
        spacing_top=100, spacing_bottom=100)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=505, image_width=635, spacing=60)
    assert_para_block_section_spacing(browser, spacing=100)

def test_para_block_links(browser, base_url):
    verify_url_by_link_text(browser, 'Turn expense reporting real-time', base_url, '/product/expenses')
    verify_url_by_link_text(browser, 'Automate corporate card reconciliations', base_url, '/product/cards')
    verify_url_by_link_text(browser, 'Check out how data flows in and out of Fyle', base_url, '/product/integrations')
    verify_url_by_link_text(browser, 'More informed decisions with all the expense', base_url, '/product/analytics')

def test_page_overflow(browser):
    assert_overflowing(browser)

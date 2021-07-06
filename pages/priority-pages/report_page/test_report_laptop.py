from common.asserts import assert_overflowing, verify_url_by_link_text
from common.components.para_blocks import *
from common.components.g2_section import *
from common.components.hero import *

from . import laptop_browser as browser

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
    assert_para_blocks(browser, para_width=518, image_width=622, spacing=60)
    assert_para_block_section_spacing(browser, spacing=100)

def test_para_block_links(browser, base_url):
    verify_url_by_link_text(browser, 'Make expense reporting seamless', base_url, '/product/expenses')
    verify_url_by_link_text(browser, 'Manage multiple card expenses', base_url, '/product/cards')
    verify_url_by_link_text(browser, 'Achieve faster employee reimbursement TAT', base_url, '/product/payments')
    verify_url_by_link_text(browser, 'Integrate with your choice of T&E tools', base_url, '/product/integrations')

def test_g2_section_spacing(browser):
    assert_g2_section_spacing(browser, 100)

def test_g2_links(browser):
    assert_g2_links(browser)

def test_g2_table(browser):
    assert_g2_table(browser)

def test_bottom_banner_cta(browser):
    assert_bottom_banner_cta(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

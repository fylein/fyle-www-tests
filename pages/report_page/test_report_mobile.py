from common.asserts import assert_overflowing, verify_url_by_link_text
from common.components.para_blocks import *
from common.components.g2_section import *
from common.components.hero import *

from . import mobile_browser as browser

def test_hero_section(browser):
    section_class = 'homepage-hero'
    assert_h1_spacing(browser, section_class, 16)
    assert_button_spacing(browser, section_class, cta=False)
    assert_customer_logo(browser, 375,
        section_xpath=f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section',
        logo_xpath=f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//div[contains(@class, "d-md-none d-block")]//img[contains(@class, "fy-container-mw-ie")]',
        spacing_bottom=50)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=440, image_width=440)
    assert_para_block_section_spacing(browser, spacing=40)

def test_para_block_links(browser, base_url):
    verify_url_by_link_text(browser, 'Make expense reporting seamless', base_url, '/product/expenses')
    verify_url_by_link_text(browser, 'Manage multiple card expenses', base_url, '/product/cards')
    verify_url_by_link_text(browser, 'Achieve faster employee reimbursement TAT', base_url, '/product/payments')
    verify_url_by_link_text(browser, 'Integrate with your choice of T&E tools', base_url, '/product/integrations')

def test_g2_section_spacing(browser):
    assert_g2_section_spacing(browser, 40)

def test_g2_links(browser):
    assert_g2_links(browser)

def test_g2_table(browser):
    assert_g2_table(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

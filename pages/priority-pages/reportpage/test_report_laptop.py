from common.asserts import assert_overflowing
from common.components.para_blocks import *
from common.components.g2_section import *
from common.asserts import verify_url_by_link_text

from . import laptop_browser as browser

def test_hero_section(browser):
    section_class = 'homepage-hero'
    assert_hero_section(browser, section_class, 1140, 1140)

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
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def test_page_overflow(browser):
    assert_overflowing(browser)

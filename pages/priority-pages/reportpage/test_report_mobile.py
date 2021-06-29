from common.asserts import assert_overflowing
from common.components.para_blocks import *
from common.components.hero import *
from common.components.g2_section import *
from common.asserts import verify_url_by_link_text

from . import mobile_browser as browser

def test_hero_section(browser):
    section_class = 'homepage-hero'
    assert_mobile_hero_section(browser, section_class)

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

from common.components.para_blocks import *
from common.asserts import *
from common.components.hero import *

from . import laptop_browser as browser

def test_hero_section(browser):
    section_class = 'product-hero'
    assert_h1_spacing(browser, section_class)
    assert_subtext_spacing(browser, section_class)
    assert_img(browser, 1140, section_class)
    assert_button_spacing(browser, section_class, value=48)
    assert_customer_logo(browser, 997,
        section_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]',
        logo_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-block")]',
        spacing_top=80
    )

def test_para_block(browser):
    assert_para_blocks(browser, para_width=518, image_width=622, spacing=60)
    assert_para_block_section_spacing(browser, spacing=100)

def test_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def test_page_overflow(browser):
    assert_overflowing(browser)

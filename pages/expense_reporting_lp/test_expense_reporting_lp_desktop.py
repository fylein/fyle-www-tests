from common.asserts import *
from common.components.para_blocks import *
from common.components.hero_img_on_right import *
from common.components.hero import assert_customer_logo

from . import desktop_browser as browser

def test_hero_section(browser):
    section_class='capterra-hero'
    assert_h1_spacing(browser, section_class)
    assert_hero_img(browser, section_class, 728)
    assert_customer_logo(browser, 1437,
        section_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]',
        logo_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-block")]',
        spacing_top=80
    )
    assert_demo_button(browser, section_class)

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=660, image_width=622, spacing=85)

def test_bottom_banner_cta(browser):
    assert_bottom_banner_cta(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

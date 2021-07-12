from common.components.slider import *
from common.asserts import *
from common.components.hero import *

from . import desktop_browser as browser

def test_hero_section(browser):
    section_class = 'product-hero'
    assert_h1_spacing(browser, section_class)
    assert_subtext_spacing(browser, section_class)
    assert_img(browser, 760, section_class)
    assert_button_spacing(browser, section_class, value=48)
    assert_customer_logo(browser, 1437,
        section_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]',
        logo_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-block")]',
        spacing_top=80
    )

def test_side_nav(browser):
    assert_slider_section(browser)

def test_slider_section_para_block(browser):
    assert_slider_section_para_block(browser, 563, 880, 85)

def test_bottom_banner_cta(browser):
    assert_bottom_banner_cta(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

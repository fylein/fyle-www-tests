from . import desktop_browser as browser
from common.components.slider import *
from common.components.hero import assert_product_hero_section
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta

def test_hero_section(browser):
    assert_product_hero_section(browser, 760, 1437)

def test_side_nav(browser):
    assert_slider_section(browser)

def test_slider_section_para_block(browser):
    assert_slider_section_para_block(browser, 563, 880, 85)

def test_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')


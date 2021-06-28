from common.components.hero import *
from common.asserts import *
from .company import *
from . import mobile_browser as browser

def test_hero_section(browser):
    section_class = 'investor-logos'
    assert_h1_spacing(browser, section_class, 16)
    assert_subtext_spacing(browser, section_class, last_span=40, mid_span=10)
    assert_customer_logo_img(browser, '//section[contains(@class, "fy-p-0")]//div[contains(@class, "container")]//img[contains(@class, "d-md-none")]', 380)

def test_why_fyle_section(browser):
    assert_why_fyle_section(browser, 40, 20, 10, 265, 426)

def test_stat_section(browser):
    assert_stat_section(browser, 20, 400, 40)

def test_fyle_journey(browser):
    assert_fyle_journey(browser, 40, '//section[contains(@class, "fyle-journey")]//div[contains(@class, "fy-xl-row")]//div[contains(@class, col)]//img[contains(@class, "d-md-block")]', 440, 20, 30)

def test_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def test_page_overflow(browser):
    assert_overflowing(browser)

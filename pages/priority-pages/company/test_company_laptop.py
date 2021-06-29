from common.components.hero import *
from common.asserts import *
from .company import *
from . import laptop_browser as browser

def test_hero_section(browser):
    section_class = 'investor-logos'
    assert_h1_spacing(browser, section_class)
    assert_subtext_spacing(browser, section_class)
    assert_customer_logo_img(browser, '//section[contains(@class, "fy-p-0")]//div[contains(@class, "container")]//img[contains(@class, "d-md-block")]', 931)

def test_why_fyle_section(browser):
    assert_why_fyle_section(browser, 100, 40, 30, 262, 847)

def test_stat_section(browser):
    assert_stat_section(browser, 50, 255, 60)

def test_fyle_journey(browser):
    assert_fyle_journey(browser, 100, '//section[contains(@class, "fyle-journey")]//div[contains(@class, "fy-xl-row")]//div[contains(@class, col)]//img[contains(@class, "d-md-block")]', 880, 40, 60)

def test_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def test_page_overflow(browser):
    assert_overflowing(browser)
from common.asserts import *
from .common.company import *
from common.components.hero import *
from . import mobile_browser as browser

def test_hero_section(browser):
    section_class = 'investor-logos'
    assert_h1_spacing(browser, section_class, 16)
    assert_subtext_spacing(browser, section_class, value=40, mid_span=10)
    assert_customer_logo(browser, 380, logo_xpath='//section[contains(@class, "fy-p-0")]//div[contains(@class, "container")]//img[contains(@class, "d-md-none")]')

def test_why_fyle_section(browser):
    assert_why_fyle_section(browser, 40, None, 10, 265, 426)

def test_stat_section(browser):
    assert_stat_section(browser, 20, None, None, 40)

def test_fyle_journey(browser):
    assert_fyle_journey(browser, 40, None, 440, 20, 30)

def test_page_overflow(browser):
    assert_overflowing(browser)

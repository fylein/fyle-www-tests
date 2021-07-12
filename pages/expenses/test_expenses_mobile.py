from common.components.slider import *
from common.components.hero import *
from common.asserts import assert_overflowing
from common.components.sneak_peek import *

from . import mobile_browser as browser

def test_hero_section(browser):
    section_class = 'product-hero'
    assert_h1_spacing(browser, section_class, 16)
    assert_customer_logo(browser, 354,
        section_xpath=f'//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]',
        logo_xpath=f'//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-none")]',
        spacing_top=40)

def test_page_overflow(browser):
    assert_overflowing(browser)

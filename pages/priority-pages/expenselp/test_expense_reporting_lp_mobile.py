from common.asserts import assert_overflowing
from common.components.para_blocks import *
from common.components.hero_img_on_right import *
from common.components.hero import assert_customer_logo

from . import mobile_browser as browser

def test_hero_section(browser):
    #assert_hero_img_on_right_section(browser, 'capterra-hero', bulletin=False)
    section_class='capterra-hero'
    assert_h1_spacing(browser, section_class, 16)
    assert_customer_logo(browser, 354,
        section_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]',
        logo_xpath='//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-none")]',
        spacing_top=40
    )

def test_para_block_spacing(browser):
    assert_para_blocks(browser, para_width=440, image_width=440)

def test_page_overflow(browser):
    assert_overflowing(browser)

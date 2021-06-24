from . import laptop_browser as browser
from common.components.slider import *
from common.components.hero import assert_product_hero_section
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta

def test_hero_section(browser):
    assert_product_hero_section(browser, 760, 997)


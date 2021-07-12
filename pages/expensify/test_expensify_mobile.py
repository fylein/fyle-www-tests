import logging

from . import mobile_browser as browser
from common.asserts import assert_overflowing
from .common.expensify import *
from common.components.hero_img_on_right import *

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class='expensify-hero'
    assert_h1_spacing(browser, section_class, 16)
    assert_bulletin(browser, section_class, spacing_top=20, spacing_bottom=43)
    assert_section_spacing(browser, section_class, spacing_top=40)

def test_switch_from_expensify(browser):
    assert_switch_from_expensify(browser, 40, 40, 20, list_spacing=10)

def test_switch_from_expensify(browser):
    cells = browser.find_many('(//section[contains(@class, "alternative-fyle-comparison")]//table)[1]//td')
    for i, el in enumerate(cells):
        browser.find(f'((//section[contains(@class, "alternative-fyle-comparison")]//table)[1]//td)[{i+1}]', scroll=True)
        if (i % 3) == 0:
            assert_spacing_all_sides(el, 20, 20, 20, 9)
        else:
            assert_spacing_all_sides(el, 20, 9, 20, 9)

def test_rating_table_cells(browser):
    assert_rating_table_cells(browser, 20, 20, 20, 20)

def test_g2_source(browser):
    assert_g2_source(browser)

def test_faq_section(browser):
    assert_faq_section(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)

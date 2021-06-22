import logging

from . import mobile_browser as browser
from common.asserts import assert_overflowing
from .expensify import *
from common.components.hero_v2 import assert_hero_v2_section

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    assert_hero_v2_section(browser, 'expensify-hero', img_width=None, bulletin=True, g2_source='https://www.g2.com/reports/momentum-grid-report-for-expense-management-winter-2020')

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
import logging

from . import laptop_browser as browser
from common.asserts import assert_overflowing
from .expensify import *
from common.components.hero_img_on_right import assert_hero_img_on_right_section

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    assert_hero_img_on_right_section(browser, 'expensify-hero', img_width=625, bulletin=True, g2_source='https://www.g2.com/reports/momentum-grid-report-for-expense-management-winter-2020')

def test_customer_logo(browser):
    assert_customer_logo(browser, width=1140, height=183)

def test_switch_from_expensify(browser):
    assert_switch_from_expensify(browser, 100, 100, 40, list_spacing=16)

def test_table_width(browser):
    assert_table_width(browser, 1003)

def test_fyle_vs_expensify_table_cells(browser):
    assert_fyle_vs_expensify_table_cells(browser, 20, 30)

def test_rating_table_cells(browser):
    assert_rating_table_cells(browser, 21, 30, 20, 30)

def test_rating_img_cells(browser):
    assert_rating_img_cells(browser, 27, 30)

def test_table_header_cells(browser):
    assert_table_header_cells(browser, 15, 30)

def test_g2_source(browser):
    assert_g2_source(browser)

def test_faq_section(browser):
    assert_faq_section(browser)

def test_page_overflow(browser):
    assert_overflowing(browser)
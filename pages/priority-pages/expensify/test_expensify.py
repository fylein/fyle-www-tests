import logging

from common.asserts import assert_overflowing, assert_customer_logo_section
from .expensify import *
from common.components.hero_v2 import assert_hero_v2_section

from . import desktop_browser as browser

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    assert_hero_v2_section(browser, 'expensify-hero', img_width=625, bulletin=True, section_spacing=80, g2_source='https://www.g2.com/reports/momentum-grid-report-for-expense-management-winter-2020')

def test_customer_logo(browser):
    assert_customer_logo_section(browser, width=1345, height=217)

def test_switch_from_expensify(browser):
    assert_switch_from_expensify(browser, 100, 100, 40, list_spacing=16)

def test_table_width(browser):
    assert_table_width(browser, 1345)

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

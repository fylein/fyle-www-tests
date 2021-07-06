import logging

from . import desktop_browser as browser
from common.asserts import assert_overflowing
from .common.expensify import *
from common.components.hero_img_on_right import *

logger = logging.getLogger(__name__)

def test_hero_section(browser):
    section_class='expensify-hero'
    assert_h1_spacing(browser, section_class)
    assert_bulletin(browser, section_class, spacing_top=30)
    assert_section_spacing(browser, section_class, spacing_top=80, spacing_bottom=80)
    assert_hero_img(browser, section_class, 625)
    assert_g2_link(browser, 'https://www.g2.com/reports/momentum-grid-report-for-expense-management-winter-2020')

def test_customer_logo(browser):
    assert_customer_logo(browser, width=1345, height=217)

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

import logging
import time
from common.asserts import assert_spacing, assert_section_spacing, assert_dimensions, assert_spacing_all_sides, verify_url

logger = logging.getLogger(__name__)

def assert_switch_from_expensify(browser, section_top, section_bottom, h2_spacing, list_spacing):
    #Assert section spacing
    section = browser.find('//section[contains(@class, "why-choose-fyle-over-expensify")]', scroll=True, scroll_by=300)
    assert_section_spacing(section, section_top, section_bottom)

    #Assert H2 spacing
    h2 = browser.find('//section[contains(@class, "why-choose-fyle-over-expensify")]//h2', scroll=True, scroll_by=300)
    assert_spacing('bottom', h2, h2_spacing)

    #Assert listed points spacing
    lists = browser.find_many('//section[contains(@class, "why-choose-fyle-over-expensify")]//li')
    for i, li in enumerate(lists):
        if i != len(lists)-1:
            browser.find(f'(//section[contains(@class, "why-choose-fyle-over-expensify")]//li)[{i+1}]', scroll=True, scroll_by=300)
            assert_spacing('bottom', li, list_spacing)

def assert_table_width(browser, width):
    tables = browser.find_many('//section[contains(@class, "alternative-fyle-comparison")]//table')
    for i, el in enumerate(tables):
        browser.find(f'(//section[contains(@class, "alternative-fyle-comparison")]//table)[{i+1}]', scroll=True)
        assert_dimensions(el, width)

def assert_fyle_vs_expensify_table_cells(browser, top_bottom, left_right):
    cells = browser.find_many('(//section[contains(@class, "alternative-fyle-comparison")]//table)[1]//td')
    for i, el in enumerate(cells):
        browser.find(f'((//section[contains(@class, "alternative-fyle-comparison")]//table)[1]//td)[{i+1}]', scroll=True)
        assert_spacing_all_sides(el, top_bottom, left_right, top_bottom, left_right)

def assert_rating_table_cells(browser, top, right, bottom, left):
    cells = browser.find_many('(//section[contains(@class, "alternative-fyle-comparison")]//table)[2]//td')
    for i, el in enumerate(cells):
        if i > 3:
            browser.find(f'((//section[contains(@class, "alternative-fyle-comparison")]//table)[2]//td)[{i+1}]', scroll=True)
            assert_spacing_all_sides(el, top, right, bottom, left)

def assert_rating_img_cells(browser, top_bottom, left_right):
    cells = browser.find_many('(//section[contains(@class, "alternative-fyle-comparison")]//table)[2]//td')
    for i, el in enumerate(cells):
        if i < 3:
            browser.find(f'((//section[contains(@class, "alternative-fyle-comparison")]//table)[2]//td)[{i+1}]', scroll=True)
            assert_spacing_all_sides(el, top_bottom, left_right, top_bottom, left_right)

def assert_table_header_cells(browser, top_bottom, left_right):
    cells = browser.find_many('//section[contains(@class, "alternative-fyle-comparison")]//table//th')
    for i, el in enumerate(cells):
        browser.find(f'(//section[contains(@class, "alternative-fyle-comparison")]//table//th)[{i+1}]', scroll=True)
        assert_spacing_all_sides(el, top_bottom, left_right, top_bottom, left_right)

def assert_g2_source(browser):
    el = browser.find('//div[contains(@class, "g2-source")]//a', scroll=True, scroll_by=300)
    time.sleep(1)
    browser.hover_and_click(el)
    browser.switch_tab_next(1)
    verify_url(browser, 'https://www.fylehq.com/alternative/expensify')

def assert_faq_section(browser):
    cards = browser.find_many('//section[contains(@class, "expensify-alternative-faq")]//div[contains(@class, "collapsible-card-header")]')
    for i, card in enumerate(cards):
        el = browser.find(f'(//section[contains(@class, "expensify-alternative-faq")]//div[contains(@class, "collapsible-card-header")])[{i+1}]', scroll=True, scroll_by=300)
        assert el and el.is_displayed, 'Header not displayed'
        browser.hover_and_click(el)
        card_body = browser.find(f'(//div[contains(@class, "collapsible-card ")])[1]//div[contains(@class, "collapsible-card-body") and contains(@class, "show")]')
        assert card_body and card_body.is_displayed(), 'FAQ dropdown is not opening'
        browser.hover_and_click(el)
        card_body = browser.find(f'(//div[(@class="collapsible-card")])[{i+1}]//div[contains(@class, "collapsible-card-body") and not(contains(@class, "show"))]')
        assert card_body, 'FAQ dropdown is not closing'

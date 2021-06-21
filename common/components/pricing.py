import logging
import time

from common.asserts import assert_overflowing, assert_spacing, assert_dimensions, assert_overlap
from common.components.steps_form import assert_steps_form_modal, close_steps_form

logger = logging.getLogger(__name__)

def get_active_plan(browser, plan):
    position = 'left'
    if plan == 'Annually':
        position = 'right'
    return browser.find(f'//div[contains(@class, "switch-field")]//label[contains(@class, "{position}") and contains(@class, "paragraph-4--medium--link--v1") and contains(text(), "{plan}")]')

def get_price_value(browser):
    standard_price = browser.find('//div[contains(@class, "pricing-info")]//p[contains(@class, "standard")]').text
    standard_price = standard_price.splitlines()[1]

    business_price = browser.find('//div[contains(@class, "pricing-info")]//p[contains(@class, "business")]').text
    business_price = business_price.splitlines()[1]

    return [standard_price, business_price]

def get_billing_text(browser):
    standard_plan_text = browser.find('(//div[contains(@class, "pricing-info")]//span[contains(@class, "text-left")])[1]').text
    standard_plan_text = standard_plan_text.split(' ')[-1]

    business_plan_text = browser.find('(//div[contains(@class, "pricing-info")]//span[contains(@class, "text-left")])[2]').text
    business_plan_text = business_plan_text.split(' ')[-1]

    return [standard_plan_text, business_plan_text]

def assert_annual_price(browser):
    #Active plan UI check
    check_box = browser.find('//div[contains(@class, "switch-field")]//input[contains(@class, "checkbox-checked")]')
    active_plan = get_active_plan(browser, 'Annually')
    assert check_box and active_plan and active_plan.is_displayed(), "Annual pricing is not active"

    #Active plan Pricing check
    active_plan_pricing = get_price_value(browser)
    assert active_plan_pricing[0] == '4.99', f'Annual standard plan pricing is incorrect'
    assert active_plan_pricing[1] == '8.99', f'Annual business plan pricing is incorrect'

    #Active plan text check
    billing_text = get_billing_text(browser)
    assert billing_text[0] == 'annually', f'Standard plan billed annually text is incorrect'
    assert billing_text[1] == 'annually', f'Business plan billed annually text is incorrect'

def assert_monthly_price(browser):
    #Active plan UI check
    browser.click('//div[contains(@class, "switch-field")]')
    check_box = browser.find('//div[contains(@class, "switch-field")]//input[not(contains(@class, "checkbox-checked"))]')
    active_plan = get_active_plan(browser, 'Monthly')
    assert check_box and active_plan and active_plan.is_displayed(), "Monthly pricing is not active"

    #Active plan Pricing check
    active_plan_pricing = get_price_value(browser)
    assert active_plan_pricing[0] == '6.99', f'Monthly standard plan pricing is incorrect'
    assert active_plan_pricing[1] == '11.99', f'Monthly business plan pricing is incorrect'

    #Active plan text check
    billing_text = get_billing_text(browser)
    assert billing_text[0] == 'monthly', f'Standard plan billed monthly text is incorrect'
    assert billing_text[1] == 'monthly', f'Business plan billed monthly text is incorrect'

def assert_toggling(browser):
    assert_monthly_price(browser)
    browser.click('//div[contains(@class, "switch-field")]')
    assert_annual_price(browser)

def assert_demo_form_buttons(browser):
    card_btns = browser.find_many('//div[contains(@class, "card-body")]//div[contains(@class, "card-btn")]')
    for btn in card_btns:
        browser.hover_and_click(btn)
        assert_steps_form_modal(browser)
        close_steps_form(browser)

def assert_card_width(browser, width=None, height=None, mid_card_height=None):
    cards = browser.find_many('//div[contains(@class, "card-group")]//div[contains(@class, "card ")]')
    for i, card in enumerate(cards):
        if i != 1:
            assert_dimensions(card, width, height)
        else:
            assert_dimensions(card, width, mid_card_height)

def assert_title_desc_width(browser, width=None, height=None):
    title_desc = browser.find_many('//section[contains(@class, "pricing")]//div[contains(@class, "card-group")]//div[contains(@class, "card-head")]//p[not(contains(@class, "card-title"))]')
    for i, desc in enumerate(title_desc):
        assert_overlap(browser, desc)
        if i != 1:
            assert_dimensions(desc, width, height)
        else:
            assert_dimensions(desc, width-2, height)

def assert_feature_list(browser, width=None):
    lists = browser.find_many('//section[contains(@class, "pricing")]//div[contains(@class, "card-body")]//div[contains(@class, "-feature")]//li')
    for i, li in enumerate(lists):
        el = browser.find(f'(//section[contains(@class, "pricing")]//div[contains(@class, "card-body")]//div[contains(@class, "-feature")]//li)[{i+1}]', scroll=True)
        assert_dimensions(el, width)
        assert_overlap(browser, el)

def assert_comparison_section(browser, scroll_to_view='false'):
    btn = browser.find('//div[contains(@class, "compare-plan")]//div[contains(@class, "btn-compare")]', scroll=True, scroll_by=300, scroll_to_view=scroll_to_view)
    time.sleep(1)
    browser.hover_and_click(btn)
    table = browser.find('//div[contains(@class, "compare-plan")]//div[contains(@class, "feature-table") and not(contains(@class, "d-none"))]', scroll=True)
    time.sleep(1)
    assert table and table.is_displayed(), 'Error in opening compare all features dropdown'

def assert_scroll_btn(browser):
    assert_comparison_section(browser)
    browser.scroll_up_or_down(-300)
    btn = browser.click('//a[@id="scroll"]//div[contains(@class, "scroll-btn")]')
    time.sleep(2)
    card_group = browser.find('//section[contains(@class, "pricing")]//div[contains(@class, "card-group")]')
    browser_height = browser.get_window_size()['height']
    limit = browser.current_scroll_position()+(browser_height * 0.25)
    assert card_group.location['y'] <= limit, 'Not scrolled to hero section'

def assert_comparison_demo_button(browser):
    assert_comparison_section(browser)
    time.sleep(1)
    buttons = browser.find_many('//div[contains(@class, "compare-plan")]//div[contains(@class, "table-column")]//button')
    for btn in buttons:
        browser.hover_and_click(btn)
        assert_steps_form_modal(browser)
        close_steps_form(browser)

def assert_sticky_header(browser, top_value=79):
    assert_comparison_section(browser)
    time.sleep(1)
    header = browser.find('//div[contains(@class, "compare-plan")]//div[contains(@class, "table-head")]')
    logger.info(header.value_of_css_property('position'))
    top = header.value_of_css_property('top')
    assert top == '0px', 'Problem in top position of feature comparison header'
    position = header.value_of_css_property('position')
    assert position == 'sticky', 'Feature comparison header is not sticky'
    browser.scroll_up_or_down(-300)
    time.sleep(1)
    top = header.value_of_css_property('top')
    assert top == f'{top_value}px', 'Problem in top position of feature comparison header'

def assert_faq_spacing(browser, section_space=None, h2_space=None):
    faq_section = browser.find('//section[contains(@class, "pricing-faq")]', scroll=True)
    assert_spacing('top', faq_section, section_space)
    assert_spacing('bottom', faq_section, section_space)
    faq_heading = browser.find('//section[contains(@class, "pricing-faq")]//h2')
    assert_spacing('bottom', faq_heading, h2_space)

def assert_faq_card_spacing(browser, card_padding=None, card_row_spacing=None):
    faq_section = browser.find('//section[contains(@class, "pricing-faq")]', scroll=True)
    faq_cards = browser.find_many('//section[contains(@class, "pricing-faq")]//div[contains(@class, "pricing-card")]')
    for card in faq_cards:
        assert_spacing('top', card, card_padding)
        assert_spacing('right', card, card_padding)
        assert_spacing('bottom', card, card_padding)
        assert_spacing('left', card, card_padding)
    if card_row_spacing:
        card_row = browser.find('//section[contains(@class, "pricing-faq")]//div[contains(@class, "row")][2]')
        assert_spacing('bottom', card_row, card_row_spacing, 'FAQ section card row spacing bottom is incorrect')

def assert_usage_led_pricing(browser, width=None, height=None):
    el = browser.find('//div[contains(@class, "usage-led")]//p', scroll=True, scroll_by=300, scroll_to_view='false')
    time.sleep(3)
    assert_dimensions(el, width, height)
    assert_overlap(browser, el)

def assert_see_details(browser):
    anchors = browser.find_many('//div[contains(@class, "feature-in-sm")]//a')
    for i, el in enumerate(anchors):
        el = browser.find(f'(//div[contains(@class, "feature-in-sm")]//a)[{i+1}]', scroll=True, scroll_by=300, scroll_to_view='false')
        browser.hover_and_click(el)
        feature_list = browser.find(f'(//div[contains(@class, "feature-in-sm")])[{i+1}]//div[contains(@class, "feature-wrapper-sm") and contains(@class, "show")]')
        assert feature_list and feature_list.is_displayed(), f'Problem in opening in {i+1} card'

        

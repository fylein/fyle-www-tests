import logging
import time

from common.asserts import assert_overflowing, assert_spacing
from common.components.steps_form import assert_steps_form_modal, close_steps_form

from . import desktop_browser as browser

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

def test_annual_price(browser):
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


def test_monthly_price(browser):
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

def test_toggling(browser):
    test_monthly_price(browser)
    browser.click('//div[contains(@class, "switch-field")]')
    test_annual_price(browser)

def test_demo_form_buttons(browser):
    card_btns = browser.find_many('//div[contains(@class, "card-body")]//div[contains(@class, "card-btn")]')
    for btn in card_btns:
        browser.hover_and_click(btn)
        assert_steps_form_modal(browser)
        close_steps_form(browser) 

def test_card_spacing(browser):
    cards = browser.find_many('//div[contains(@class, "card-group")]//div[contains(@class, "card ")]')
    for i, card in enumerate(cards):
        assert_spacing('right', card, 25)
        if i != 0:
            assert_spacing('left', card, 25)
        else:
            assert_spacing('left', card, 165)

def test_compare_button(browser):
    btn = browser.find('//div[contains(@class, "compare-plan")]//div[contains(@class, "btn-compare")]', scroll=True, scroll_by=300)
    time.sleep(1)
    browser.hover_and_click(btn)
    table = browser.find('//div[contains(@class, "compare-plan")]//div[contains(@class, "feature-table") and not(contains(@class, "d-none"))]', scroll=True)
    time.sleep(1)
    assert table and table.is_displayed(), 'Error in opening compare all features dropdown'

    #Assert scroll top
    browser.scroll_up_or_down(-300)
    btn = browser.click('//a[@id="scroll"]//div[contains(@class, "scroll-btn")]')
    time.sleep(2)


def test_faq_spacing(browser):
    faq_section = browser.find('//section[contains(@class, "pricing-faq")]', scroll=True)
    assert_spacing('top', faq_section, 100)
    assert_spacing('bottom', faq_section, 100)
    faq_heading = browser.find('//section[contains(@class, "pricing-faq")]//h2')
    assert_spacing('bottom', faq_heading, 40)

def test_faq_card_spacing(browser):
    faq_section = browser.find('//section[contains(@class, "pricing-faq")]', scroll=True)
    faq_cards = browser.find_many('//section[contains(@class, "pricing-faq")]//div[contains(@class, "pricing-card")]')
    for card in faq_cards:
        assert_spacing('top', card, 40)
        assert_spacing('right', card, 40)
        assert_spacing('bottom', card, 40)
        assert_spacing('left', card, 40)
    
    card_row = browser.find('//section[contains(@class, "pricing-faq")]//div[contains(@class, "row")][2]')
    assert_spacing('bottom', card_row, 30, 'FAQ section card row spacing bottom is incorrect')

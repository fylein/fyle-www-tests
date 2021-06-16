import logging

from common.asserts import assert_overflowing

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
    
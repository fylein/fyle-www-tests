from common.asserts import *

def assert_g2_section_spacing(browser, section_spacing, h2_spacing=20, span_spacing=20):
    section = browser.find('//section[contains(@class, "all-alternative-comparison")]', scroll=True, scroll_by=300)
    assert_spacing('top', section, section_spacing)

    h2 = browser.find('//section[contains(@class, "all-alternative-comparison")]//h2', scroll=True, scroll_by=300)
    assert_spacing('bottom', h2, h2_spacing)

    spans = browser.find_many('//section[contains(@class, "all-alternative-comparison")]//div[contains(@class, "col-lg-10")]//p')
    for i, el in enumerate(spans):
        assert_spacing('bottom', el, span_spacing)

def assert_g2_links(browser):
    link = browser.find_by_link_text('G2 reviews', scroll=True, scroll_by=300)
    browser.hover_and_click(link)
    switch_tab_and_verify_url(browser, 'https://www.g2.com/')

    review_button = browser.find('//section[contains(@class, "all-alternative-comparison")]//div[contains(@class, "read-reviews")]//a', scroll=True, scroll_by=300)
    browser.hover_and_click(review_button)
    switch_tab_and_verify_url(browser, 'https://www.g2.com/products/fyle/reviews')

    sleep(1)
    g2_source = browser.find_by_link_text('Source: G2 Crowd', scroll=True, scroll_by=300)
    browser.hover_and_click(g2_source)    
    switch_tab_and_verify_url(browser, 'https://www.g2.com/compare/fyle-vs-sap-concur-vs-expensify-vs-certify-by-emburse')

def assert_g2_table(browser):
    features = browser.find_many('//div[contains(@class, "feature-comparison-box")]//div[contains(@class, "accordion-toggle")]')
    for i, el in enumerate(features):
        el = browser.find(f'//div[contains(@class, "feature-comparison-box")]//div[contains(@class, "accordion-toggle")][{i+1}]', scroll=True, scroll_by=300)
        # Not clicking on the first row since it's already opened.
        if i != 0:
            browser.hover_and_click(el)
        # Finding the element expanded_el which is the same el element but using different Xpath, where aria-expanded=true
        expanded_el = browser.find(f'//div[contains(@class, "feature-comparison-box")]//div[@aria-expanded="true"]')
        # If Xpath can find expanded_el then el == expanded_el, if not the dropdown down is not opened on click or arai-expanded=false.
        assert el == expanded_el and expanded_el.is_displayed(), 'Dropdown not opening in comparison table'
        browser.hover_and_click(el)
        closed_el = browser.find(f'//div[contains(@class, "feature-comparison-box")]//div[@aria-expanded="false"][{i+1}]')
        assert el == closed_el, "Dropdown not closing in comparison table"

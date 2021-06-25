import logging
from common.asserts import assert_element_width
from common.utils import get_resolution


logger = logging.getLogger(__name__)

def is_sneak_peek_open(browser, i, j):
    el = browser.find(f'(//section[contains(@class, "new-sneak-peek-collapse-section")])[{i+1}]//div[contains(@class, "collapse-card")][{j+1}]', scroll=True, scroll_by=-250, scroll_to_view='true')
    collapse_class = el.get_attribute('class').split(' ')[-1]
    if collapse_class == 'collapse-open':
        return True
    return False

def assert_sneak_peek_section(browser, text_width=0, img_width=0):
    browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]', scroll=True)

    if get_resolution(browser) != 'mobile_1':
        text_col = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "sneak-peek-text-col")]', scroll=True)
        assert_element_width(text_col, text_width)
        img_col = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "sneak-peek-img-col")]', scroll=True)
        assert_element_width(img_col, img_width)
        collapsible_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(concat(@class, " "), "collapsible-card ")]')
        for i in range(len(collapsible_card)):
            card_header = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card")]//div[contains(@id, "card-{i+1}-heading")]', scroll=True)
            browser.click_element(card_header)
            card_body = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card expanded") and contains(@id, "card-{i+1}")]', scroll=True)
            assert card_body and card_body.is_displayed(), 'Sneak peek click not working'

    else:
        sections = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]')
        collapse_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//a[contains(@class, "collapse-arrow")]')
        for i in range(len(sections)):
            collapse_card = browser.find_many(f'//section[contains(@class, "new-sneak-peek-collapse-section")][{i+1}]//a[contains(@class, "collapse-arrow")]')
            for j in range(len(collapse_card)):
                el = browser.find(f'(//section[contains(@class, "new-sneak-peek-collapse-section")][{i+1}]//a[contains(@class, "collapse-arrow")])[{j+1}]', scroll=True, scroll_by=-250, scroll_to_view='true')
                if is_sneak_peek_open(browser, i, j):
                    browser.hover_and_click(el)
                    assert not is_sneak_peek_open(browser, i, j), 'Sneak peek section not closing'
                else:
                    browser.hover_and_click(el)
                    assert is_sneak_peek_open(browser, i, j), 'Sneak peek section not opening'

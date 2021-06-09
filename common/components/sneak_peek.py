# import logging
# from common.asserts import assert_element_width
# from ..utils import get_resolution

# logger = logging.getLogger(__name__)

# def assert_sneak_peek_section(browser, text_width=0, img_width=0):
#     browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]', scroll=True)

#     if get_resolution(browser) != 'mobile_1':
#         text_col = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "sneak-peek-text-col")]', scroll=True)
#         assert_element_width(text_col, text_width)
#         img_col = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "sneak-peek-img-col")]', scroll=True)
#         assert_element_width(img_col, img_width)
#         collapsible_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(concat(@class, " "), "collapsible-card ")]')
#         for i, card in enumerate(collapsible_card):
#             card_header = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card")]//div[contains(@id, "card-{i+1}-heading")]', scroll=True)
#             browser.click_element(card_header)
#             card_body = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card expanded") and contains(@id, "card-{i+1}")]', scroll=True)
#             assert card_body and card_body.is_displayed(), 'Sneak peek click not working'

#     # else:
#     #     collapse_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(concat(@class, " "), " collapse-card")]')

#     #     for i, card in enumerate(collapse_card):
#     #         xpath = f'(//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card")])[{i+1}]'
#     #         card = browser.find(xpath=xpath, scroll=True)
#     #         if i == 0:
#     #             xpath = f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1} collapse-card collapse-open")]'
#     #             card = browser.find(xpath=xpath)
#     #             assert card, 'The first card of the sneak peek section is not opened!'
#     #             xpath = f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1} collapse-card collapse-open")]//a[contains(@class, "collapse-arrow")]'
#     #             card = browser.find(xpath=xpath)
#     #             assert card, 'Element not found'
#     #             time.sleep(3)
#     #             card = browser.click(xpath=xpath)
#     #             logger.info(card)
#     #             assert card, 'Unable to click'
#     #             time.sleep(3)
#     #             card = browser.find(xpath=f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1}")]//div[contains(@class, "sneak-peek-mobile-card d-none")]')
#     #             assert card, 'Error in closing the card'
#     #         #if i != 0:
#     #             # xpath = f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1} collapse-card")]//a[contains(@class, "collapse-arrow")]'
#     #             # card = browser.find(xpath=xpath, scroll=True)
#     #             # logger.info(card)
#     #             # # assert card, 'Unable to find'
#     #             # card = browser.click(xpath=xpath)
#     #             # assert card, 'Unable to click'
#     #             # xpath=f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1} collapse-card collapse-open")]//a[contains(@class, "collapse-arrow")]'
#     #             # card = browser.find(xpath=xpath, scroll=True)
#     #             # assert card, 'Error in opening the card'
#     #             # card = browser.click(xpath=xpath)
#     #             # assert card, 'Unable to click'
#     #             # card = browser.find(xpath='//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapse-card-heading{i+1}")]//div[contains(@class, "sneak-peek-mobile-card d-none")]')
#     #             # assert card, 'Error in closing the card'

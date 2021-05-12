import time
import logging

logger = logging.getLogger(__name__)

def assert_sneak_peek_section(browser):
  section = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]', scroll=True)
  collapsible_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(concat(@class, " "), "collapsible-card ")]')

  for i, card in enumerate(collapsible_card):
    card_header = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card")]//div[contains(@id, "card-{i+1}-heading")]', scroll=True)
    #logger.info(card_header)
    browser.click_element(card_header)
    card_body = browser.find(f'//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card expanded") and contains(@id, "card-{i+1}")]', scroll=True)
    #logger.info(card_body)
    assert card_body and card_body.is_displayed(), 'Sneak peek click not working'
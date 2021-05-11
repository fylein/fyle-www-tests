import time
import logging

logger = logging.getLogger(__name__)

def assert_sneak_peek_section(browser):
  section = browser.find('//section[contains(@class, "new-sneak-peek-collapse-section")]')
  collapsible_card = browser.find_many('//section[contains(@class, "new-sneak-peek-collapse-section")]//div[contains(@class, "collapsible-card")]')
  for i, card in enumerate(collapsible_card):
    card_header = card.find_element_by_id(f'card-{i+1}-heading')
    logger.info(card_header)
    browser.click_element(card_header)
    card_body = card.find_element_by_class_name('show')
    assert card_body and card_body.is_displayed(), 'Sneak peek click not working'
import time
import logging

from common.asserts import assert_cards_redirection

logger = logging.getLogger(__name__)

def assert_resources_section(browser, links):
  section_xpath = '//section[contains(@class, "expense-report-bottom-card-section")]'
  cards_xpath = '//section[contains(@class, "expense-report-bottom-card-section")]//div[contains(@class, "cards-row")]//div//a[contains(@class, "feature-cards")]'
  assert_cards_redirection(browser, section_xpath, cards_xpath, links)


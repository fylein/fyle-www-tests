import logging

from common.asserts import assert_cards_redirection

logger = logging.getLogger(__name__)

def assert_resources_section(browser, base_url, links):
    cards_xpath = '//section[contains(@class, "expense-report-bottom-card-section")]//div[contains(@class, "cards-row")]//div//a[contains(@class, "feature-cards")]'
    assert_cards_redirection(browser, base_url, cards_xpath, links)

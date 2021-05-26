import logging

from common.asserts import assert_cards_redirection

logger = logging.getLogger(__name__)

def assert_back_links_card(browser, base_url, links):
    cards_xpath = '//section[contains(@class, "cross-linking ")]//div[contains(@class, "cross-link-row")]//div[contains(@class, "card ")]'
    assert_cards_redirection(browser, base_url, cards_xpath, links)

def assert_back_links_text(browser, base_url, links):
    links_xpath = '//section[contains(@class, "cross-linking-2 ")]//div[contains(@class, "cross-link-row")]//a[contains(@class, "description-link card-link")]'
    assert_cards_redirection(browser, base_url, links_xpath, links)


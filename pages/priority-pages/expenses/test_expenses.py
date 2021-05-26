import logging

from common.asserts import assert_overflowing
from common.components.backlinks import assert_back_links_card, assert_back_links_text
from common.components.slider import assert_slider_section

from . import desktop_browser as browser

def test_back_link_card(browser, base_url):
    links = ['/product/cards', '/product/integrations']
    assert_back_links_card(browser, base_url, links)

def test_back_link_text(browser, base_url):
    links = ['/product/approvals', '/product/compliance', '/product/payments', '/product/analytics']
    assert_back_links_text(browser, base_url, links)

def test_slider_section(browser):
    assert_slider_section(browser)

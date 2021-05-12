import time
import logging
import pytest

from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_links
from common.components.para_blocks import assert_para_blocks
from homepage import desktop_browser as browser
from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names
# from common.components.demo_form import test_bad_email
from common.components.resources import assert_resources_section
from common.components.sneak_peek import assert_sneak_peek_section

logger = logging.getLogger(__name__)


def test_bad_email(browser):
    assert_bad_email(browser, email="tes#.")

def test_non_business_email(browser):
    assert_non_business_email(browser)

def test_invalid_names(browser):
    assert_invalid_names(browser, first_name="first test", last_name="last test")

def test_page_overflow(browser):
    assert_overflowing(browser)

def test_para_blocks(browser):
    assert_para_blocks(browser, para_width=660, image_width=880, spacing=85)

def test_required_fields(browser):
    assert_required_fields(browser)

def test_success(browser):
    assert_success(browser)

def test_sneak_peek_section(browser):
    assert_sneak_peek_section(browser)

def test_resources_section(browser, base_url):
    links = [f'{base_url}/resources/expense-management-roi-calculator', f'{base_url}/resources/ebooks/automate-travel-expense-management', f'{base_url}/resources']
    assert_resources_section(browser, links)

# @pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
# def test_blog_link(browser):
#     blog_link = "(//div[contains(@class, 'resources-links')]//a[contains(text(), 'Blog')])"
#     link = 'https://ww2.fylehq.com/blog'
#     blog_body = "//body[contains(@class, 'body-2')]"
#     assert_links(browser, blog_link, link, blog_body)

# @pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
# def test_help_link(browser):
#     help_link = "(//div[contains(@class, 'resources-links')]//a[contains(text(), 'Help articles')])"
#     link = 'https://ww2.fylehq.com/help/en'
#     help_body = "//div[contains(@class, 'content')]"
#     assert_links(browser, help_link, link, help_body)
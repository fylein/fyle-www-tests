import time
import logging
import pytest

from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_links
from common.utils import resize_browser
from common.components.para_blocks import assert_para_blocks
from homepage import browser
from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names
# from common.components.demo_form import test_bad_email
from common.components.resources import assert_resources_section
from common.components.sneak_peek import assert_sneak_peek_section

logger = logging.getLogger(__name__)

# @pytest.fixture(params=[('desktop_1')], scope='function')
# def browser(module_browser, base_url, request):
#     resize_browser(browser=module_browser, resolution=request.param)
#     module_browser.get(base_url + '/')
#     #time.sleep(4)
#     site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
#     module_browser.hover(site_element)
#     return module_browser

# Form = DemoForm()
#Check demo form (common section)
def test_bad_email(browser):
    logging.info('Checking bad email...')
    assert_bad_email(browser)

# def test_required_fields(browser):
#     assert_required_fields(browser)

# def test_non_business_email(browser):
#     assert_non_business_email(browser)

# def test_invalid_names(browser):
#     assert_invalid_names(browser)

# def test_success(browser):
#     assert_success(browser)

# def test_page_overflow(browser):
#     assert_overflowing(browser)

# def test_para_blocks(browser):
#     assert_para_blocks(browser)

# def test_sneak_peek_section(browser):
#     assert_sneak_peek_section(browser)

# @pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
# def test_resources_section(browser):
#     links = ['http://localhost:4000/resources/expense-management-roi-calculator', 'http://localhost:4000/resources/ebooks/automate-travel-expense-management', 'http://localhost:4000/resources/']
#     assert_resources_section(browser, links)

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
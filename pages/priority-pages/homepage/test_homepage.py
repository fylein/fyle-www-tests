import time
import logging
import pytest

from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_left_right_para_block, assert_links
from common.utils import resize_browser
from common.para_blocks.para_blocks import assert_para_blocks
from common.test_getdemo import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/')
    #time.sleep(4)
    site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
    module_browser.hover(site_element)
    return module_browser


#Check demo form (common section)
@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_bad_email(browser):
    assert_bad_email(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_required_fields(browser):
    assert_required_fields(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_non_business_email(browser):
    assert_non_business_email(browser=browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_invalid_names(browser):
    assert_invalid_names(browser=browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_success(browser):
    assert_success(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_page_overflow(browser):
    assert_overflowing(browser=browser)


@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_para_block(browser):
    assert_para_blocks(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_blog_link(browser):
    blog_link = "(//div[contains(@class, 'resources-links')]//a[contains(text(), 'Blog')])"
    link = 'https://ww2.fylehq.com/blog'
    blog_body = "//body[contains(@class, 'body-2')]"
    assert_links(browser, blog_link, link, blog_body)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_help_link(browser):
    help_link = "(//div[contains(@class, 'resources-links')]//a[contains(text(), 'Help articles')])"
    link = 'https://ww2.fylehq.com/help/en'
    help_body = "//div[contains(@class, 'content')]"
    assert_links(browser, help_link, link, help_body)
import time
import logging
import pytest

from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_left_right_para_block, assert_links
from common.utils import resize_browser
from common.test_getdemo import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/')
    time.sleep(4)
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

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_product_features_section(browser):
    if not browser.is_desktop():
        browser.refresh()

    card_urls = [
        'https://ww2.fylehq.com/product/expenses',
        'https://ww2.fylehq.com/product/cards',
        'https://ww2.fylehq.com/product/approvals',
        'https://ww2.fylehq.com/product/compliance',
        'https://ww2.fylehq.com/product/budgets',
        'https://ww2.fylehq.com/product/payments',
        'https://ww2.fylehq.com/product/analytics',
        'https://ww2.fylehq.com/product/integrations',
        'https://ww2.fylehq.com/product/finance-operations'
    ]
    card_list_desktop = [
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Expenses')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Cards')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Approvals')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Compliance')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Budgets')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Payments')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Analytics')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Integrations')]//parent::*//parent::*",
        "//section[contains(@class, 'home-page-features')]//a[contains(@class, 'container-wrapper')]//h5[contains(text(), 'Finance ops')]//parent::*//parent::*"
    ]

    assert_cards_redirection(browser, card_list_desktop, card_urls, same_tab=True)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_home_testimonial(browser):
    assert_home_testimonial(browser)

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

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_para_block(browser):
    left_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img homepage')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-left-para-padding--70')]")
    right_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img homepage')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-right-para-padding--70')]")
    assert_left_right_para_block(browser, left_blocks, right_blocks, 70)

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_modal_open(browser):
    browser.click("//section[contains(@class, 'homepage-hero')]//div[contains(@class, 'hero-cta')]//a")
    modal = browser.find("//div[@id = 'contact-us-modal']")
    assert modal.is_displayed(), 'Modal is not opened'

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_modal_open_bottom(browser):
    browser.refresh()
    browser.click("//section[contains(@class, 'homepage-deepdive-section')]//div[contains(@class, 'cta-container')]//a")
    modal = browser.find("//div[@id='contact-us-modal']")
    assert modal.is_displayed(), 'Modal is not opened'

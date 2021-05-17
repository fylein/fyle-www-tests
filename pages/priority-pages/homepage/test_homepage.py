import time
import logging
import pytest

from pytest import mark as m

from common.asserts import assert_overflowing, assert_cards_redirection, assert_home_testimonial, assert_links, test
from common.components.para_blocks import assert_para_blocks
from homepage import desktop_browser as browser
from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names
# from common.components.demo_form import test_bad_email
from common.components.resources import assert_resources_section
from common.components.sneak_peek import assert_sneak_peek_section
from common.components.find_element import find
from common.components.click_element import click

logger = logging.getLogger(__name__)


@m.describe("Demo form test suit")
@m.it("Should test bad-emial")
def test_bad_email(browser):
    # click('Get a demo')
    # input('Work Email', 'value')
    # click('Get a demo')
    # validate('Work email', 'Validation text......')
    #logger.info('Testing bad email valdiation...')
    assert_bad_email(browser, email="tes#.")

@m.it("Should test non business email")
def test_non_business_email(browser):
    # - click('Get a demo')
    # - input('Work Email', 'test@gmail.com')
    # - input('First name', 'name1')
    # - input('Last name', 'name2')
    # - input('Phone', '43434343')
    # - input('Select company size', '6 to 25')
    # - input('I agree to Fyle\'s terms and conditions, and provide consent to send me communication.', True)
    # - click('Get a demo')
    # - Validate('Work email', 'Validation text......')
    #logger.info('Testing non-business email valdiation...')
    assert_non_business_email(browser)

def test_invalid_names(browser):
    logger.info('Testing invalid email valdiation...')
    assert_invalid_names(browser, first_name="first test", last_name="last test")

def test_required_fields(browser):
    assert_required_fields(browser)

def test_success(browser):
    assert_success(browser)

def test_page_overflow(browser):
    logger.info('Testing page overflow...')
    #- scroll_left()
    assert_overflowing(browser)

def test_para_blocks(browser):
    assert_para_blocks(browser, para_width=660, image_width=880, spacing=85)


def test_sneak_peek_section(browser):
    - find('There’s more to cloud expense management')
    - click('Eliminate overhead costs')
    - is_displayed(dropdown, True)
    - is_displayed(img)
    assert_sneak_peek_section(browser)
    pass

def test_resources_section(browser, base_url):
    # - Find the section('section heading')
    # - Find the card
    # - Click on that card('card heading')
    # - Switch to next tab
    # - Verify the URL('/url...')
    # - Close the tab
        # find(browser, 'Resources to streamline your expense reporting')
    # click(browser, 'ROI Calculator')
    links = ['/resources/expense-management-roi-calculator', '/resources/ebooks/automate-travel-expense-management', '/resources']
    # assert_resources_section(browser, base_url, links)
    test('should find the section', find(browser, 'Resources to streamline your expense reporting'))
    test('should click on the button', click(browser, 'ROI Calculator'))


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
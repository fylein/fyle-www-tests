import logging

from common.asserts import assert_overflowing
from common.components.navbar import assert_mobile_navbar
from common.components.footer import assert_mobile_footer
from common.components.hero import assert_mobile_hero_section
from common.asserts import verify_url_by_link_text
from common.components.para_blocks import assert_para_blocks

# from common.components.demo_form import assert_bad_email, assert_required_fields, assert_success, assert_non_business_email, assert_invalid_names

from homepage import mobile_browser as browser

logger = logging.getLogger(__name__)

# def test_hero_section(browser):
#     section_class = 'homepage-hero'
#     assert_mobile_hero_section(browser, section_class)

# def test_para_block_spacing(browser):
#     assert_para_blocks(browser, para_width=440, image_width=440)

# def test_para_block_links(browser, base_url):
#     verify_url_by_link_text(browser, 'Turn expense reporting real-time', base_url, '/product/expenses')
#     verify_url_by_link_text(browser, 'Automate corporate card reconciliations', base_url, '/product/cards')
#     verify_url_by_link_text(browser, 'Check out how data flows in and out of Fyle', base_url, '/product/integrations')
#     verify_url_by_link_text(browser, 'More informed decisions with all the expense', base_url, '/product/analytics')

def test_navbar(browser, base_url):
    assert_mobile_navbar(browser, base_url)

# def test_footer(browser, base_url):
#     assert_mobile_footer(browser, base_url)

# def test_page_overflow(browser):
#     assert_overflowing(browser=browser)

#Check demo form (common section)
# def test_bad_email(browser):
#     assert_bad_email(browser)

# def test_required_fields(browser):
#     assert_required_fields(browser)

# def test_non_business_email(browser):
#     assert_non_business_email(browser)

# def test_invalid_names(browser):
#     assert_invalid_names(browser)

# def test_success(browser):
#     assert_success(browser)

# def test_resources_section(browser, base_url):
#     links = ['/resources/expense-management-roi-calculator', '/resources/ebooks/automate-travel-expense-management', '/resources']
#     assert_resources_section(browser, base_url, links)

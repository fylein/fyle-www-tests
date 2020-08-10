from time import sleep
import logging
import pytest

from common.utils import resize_browser
from common.asserts import assert_cards_redirection
from common.asserts import assert_cta_click_and_modal_show
from common.asserts import assert_collapsible_feature_comparison_table

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + "/expense-report-software")
    return module_browser

#OTHER TEST CASES WHICH ARE PENDING TO BE ADDED HERE
#- Company logos section
#- Testimonial section

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_hero_section_cta(browser):
    cta_xpath = '//section[contains(@class, "new-hero")]//div[not(contains(@class, "demo-button-until-banner"))]/a'
    assert_cta_click_and_modal_show(browser, cta_xpath)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_g2_review_table(browser):
    assert_collapsible_feature_comparison_table(browser)

@pytest.mark.parametrize('browser', [('desktop_1'), ('mobile_1')], indirect=True)
def test_bottom_section_cards(browser):
    cards = browser.find_many(xpath='//section[contains(@class, "expense-report-bottom-card-section")]//div[contains(@class, "cards-row")]//div')
    redirect_to_urls = [
        'https://www.youtube.com/watch?v=1UuYrRacA5U',
        'https://ww2.fylehq.com/case-study/3cx-cypress-simplifies-expense-management',
        'https://ww2.fylehq.com/expense-policy/guide',
        'https://ww2.fylehq.com/resources/expense-management-roi-calculator'
    ]
    assert_cards_redirection(browser, cards, redirect_to_urls)

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_bottom_section_cta(browser):
    cta_xpath = '//section[contains(@class, "feature-bottom-section")]//a'
    assert_cta_click_and_modal_show(browser, cta_xpath)

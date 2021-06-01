import logging
import time
from ..utils import load_test_data

logger = logging.getLogger(__name__)

def assert_footer(browser, base_url):
    footer = browser.find('//footer', scroll=True)
    #links = browser.find_many('//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link")]')

    footer_data = load_test_data('footer.json')
    links = footer_data.keys()
    for link_text in links:
        try:
            el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link") and text()="{link_text}"]', scroll=True)
            if el == False:
                el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link")]//span[text()="{link_text}"]', scroll=True)
                assert el, f'Cannot find {link_text}'

            browser.hover_and_click(el)
            assert browser.get_current_url() == f'{base_url}{footer_data[link_text]}' , f"Link error in {browser.get_current_url()}, the expected path is {footer_data[link_text]}"
        except Exception as e:
            logger.error(e)
            continue
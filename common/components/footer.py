import logging
import time
from ..utils import load_test_data
from ..asserts import verify_url, find

logger = logging.getLogger(__name__)

def assert_footer(browser, base_url):
    footer_data = load_test_data('footer.json')
    links = footer_data.keys()
    i = 0
    for link_text in links:
        try:
            if link_text != 'external_links':
                el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link") and text()="{link_text}"]', scroll=True)
                if el == False:
                    el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link")]//span[text()="{link_text}"]', scroll=True)
                assert el, f'Cannot find {link_text}'

                browser.hover_and_click(el)
                verify_url(browser, f'{base_url}{footer_data[link_text]}')
                i += 1
            else:
                external_links = footer_data['external_links'].keys()
                for link_text in external_links:
                    logger.info(link_text)
                    el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-md-none"))]//a[contains(@class, "sub-link") and text()="{link_text}"]', scroll=True)
                    browser.hover_and_click(el)
                    verify_url(browser, f'{base_url}{footer_data["external_links"][link_text]}')
                    browser.back()
                    browser.activate_page()
                    i += 1
        except Exception as e:
            logger.error(e)
            continue
    logger.info(f'No.of links tested - {i}')

def assert_mobile_footer(browser, base_url):
    footer_data = load_test_data('footer.json')
    links = footer_data.keys()
    i = 0
    for link_text in links:
        try:
            if link_text != 'external_links':
                el = find(browser, f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-none d-md-none"))]//a[contains(@class, "sub-link") and text()="{link_text}"]', scroll=True)
                if el == False:
                    el = find(browser, f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-none d-md-none"))]//a[contains(@class, "sub-link")]//span[text()="{link_text}"]', scroll=True)
                assert el, f'Cannot find {link_text}'
                browser.hover_and_click(el)
                verify_url(browser, f'{base_url}{footer_data[link_text]}')
                i += 1
            else:
                external_links = footer_data['external_links'].keys()
                for link_text in external_links:
                    logger.info(link_text)
                    el = browser.find(f'//footer//div[contains(@class, "footer-col")]//div[not(contains(@class, "d-none d-md-none"))]//a[contains(@class, "sub-link") and text()="{link_text}"]', scroll=True)
                    browser.hover_and_click(el)
                    verify_url(browser, f'{base_url}{footer_data["external_links"][link_text]}')
                    browser.back()
                    browser.activate_page()
                    i += 1
        except Exception as e:
            logger.error(e)
            continue
    logger.info(f'No.of links tested - {i}')

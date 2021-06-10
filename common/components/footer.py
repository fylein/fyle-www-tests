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
                el = browser.find_by_link_text(link_text, partial=False, scroll=True, scroll_by=300)
                assert el, f'Cannot find {link_text}'
                time.sleep(1)
                browser.hover_and_click(el)
                verify_url(browser, f'{base_url}{footer_data[link_text]}')
                i += 1
            else:
                external_links = footer_data['external_links'].keys()
                for link_text in external_links:
                    el = browser.find_by_link_text(link_text, partial=False, scroll=True, scroll_by=300)
                    assert el, f'Unable to find {link_text}'
                    time.sleep(1)
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
                el = browser.find_by_link_text(link_text, partial=False, scroll=True, scroll_by=300)
                assert el, f'Cannot find {link_text}'
                time.sleep(0.5)
                browser.hover_and_click(el)
                verify_url(browser, f'{base_url}{footer_data[link_text]}')
                i += 1
            else:
                external_links = footer_data['external_links'].keys()
                for link_text in external_links:
                    el = browser.find_by_link_text(link_text, partial=False, scroll=True, scroll_by=300)
                    assert el, f'Unable to find {link_text}' 
                    time.sleep(0.5)
                    browser.hover_and_click(el)
                    verify_url(browser, f'{base_url}{footer_data["external_links"][link_text]}')
                    browser.back()
                    browser.activate_page()
                    i += 1
        except Exception as e:
            logger.error(e)
            continue
    logger.info(f'No.of links tested - {i}')

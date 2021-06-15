import logging
import time

from ..utils import load_test_data
from ..asserts import find, verify_url

logger = logging.getLogger(__name__)

def open_dropdown(browser, i):
    for attempt in range(5):
        try:
            el = find(browser, xpath=f'(//nav//li[contains(@class, "has-dropdown")])[{i+1}]', scroll=True)
            assert el, f'Unable to find nav element'
            el = browser.hover_and_click(el)
            drop_down = browser.find(xpath='//nav//div[contains(@class, "is-dropdown-visible")]')
            time.sleep(1)
            assert drop_down and drop_down.is_displayed(), 'Drop down is not opening'
            time.sleep(0.5)
            drop_down_section = browser.find(xpath=f'(//nav//ul[contains(@id, "nav-product-child-node")]//li)[{i+1}][contains(@class, "active")]')
            assert drop_down_section and drop_down_section.is_displayed(), f'Incorrect section was opened'
        except (AssertionError, AttributeError) as e:
            logger.info(attempt)
            if attempt < 4:
                logger.info(e)
                browser.refresh()
                browser.activate_page()
                time.sleep(1)
                continue
            else:
                raise
        break

def assert_navbar(browser, base_url):
    nav_data = load_test_data('navbar.json')
    nav_drop_down_elements = browser.find_many(xpath='//nav//li[contains(@class, "has-dropdown")]')
    for i, el in enumerate(nav_drop_down_elements):
        links = nav_data[i].keys()
        for j, link_text in enumerate(links):
            if link_text != 'bottom_link':
                browser.activate_page()
                open_dropdown(browser, i)
                link_element = browser.find(xpath=f'(//nav//ul[contains(@id, "nav-product-child-node")]//li)[{i+1}][contains(@class, "active")]//a[contains(@class, "hover-effect")]//span[contains(text(), "{link_text}")]')
                assert link_element and link_element.is_displayed(), f'Link element {link_text} not found'
                browser.hover_and_click(link_element)
                logger.info(nav_data[i][link_text])
                verify_url(browser, f'{base_url}{nav_data[i][link_text]}')
                if link_text == 'Blog':
                    browser.back()
                    time.sleep(1)
            else:
                bottom_links = nav_data[i]['bottom_link'].keys()
                for link_text in bottom_links:
                    browser.activate_page()
                    open_dropdown(browser, i)
                    drop_down_bottom_link = browser.find(f'(//nav//ul[contains(@id, "nav-product-child-node")]//li)[{i+1}][contains(@class, "active")]//div[contains(@class, "dropdown-bottom-link")]//a[contains(text(), "{link_text}")]')
                    assert drop_down_bottom_link and drop_down_bottom_link.is_displayed(), f'Link element {link_text} not found'
                    browser.hover_and_click(drop_down_bottom_link)
                    verify_url(browser, f'{base_url}{nav_data[i]["bottom_link"][link_text]}')

def open_mobile_navbar(browser):
    time.sleep(0.5)
    hamburger_icon = browser.click('//nav//span[contains(@class, "hamburger-icon")]')
    drop_down_container = browser.find('//div[contains(@class, "navbar-mobile") and contains(@class, "show")]')
    assert drop_down_container and drop_down_container.is_displayed(), "Mobile navbar not opening"

def open_mobile_dropdown(browser, i, el):
    el = browser.find(f'(//div[contains(@class, "link-header")])[{i+1}]', scroll=True, scroll_by=-200, scroll_to_view='true')
    assert el and el.is_displayed, f'{i+1} - Link header not found'
    browser.hover_and_click(el)
    drop_down_open = browser.find(f'(//div[contains(@class, "navlink-sm-style")])[{i+1}]//div[contains(@class, "link-header") and not(contains(@class, "navtab-closed"))]')
    assert drop_down_open and drop_down_open.is_displayed(), "Drop down is not opening"

def close_mobile_navbar(browser):
    close_icon = browser.click('//nav//span[contains(@class, "mobile-close")]')
    drop_down_container = browser.find('//div[contains(@class, "navbar-mobile") and not(contains(@class, "show"))]')
    assert drop_down_container, "Mobile navbar not closing"

                
def assert_mobile_navbar(browser, base_url):
    nav_data = load_test_data('navbar.json')
    open_mobile_navbar(browser)
    nav_drop_down_elements = browser.find_many('//div[contains(@class, "navlink-sm-style")]')
    close_mobile_navbar(browser)

    for i, el in enumerate(nav_drop_down_elements):
        links = nav_data[i].keys()

        for j, link_text in enumerate(links):
            if link_text != 'bottom_link':
                browser.activate_page()
                open_mobile_navbar(browser)
                open_mobile_dropdown(browser, i, el)
                link_element = browser.find(xpath=f'(//div[contains(@class, "navlink-sm-style")])[{i+1}]//div[contains(@class, "sm-collapse")]//a[contains(text(), "{link_text}")]', scroll=True, scroll_by=-200, scroll_to_view='true')
                if link_element == False:
                    link_element = browser.find(f'(//div[contains(@class, "navlink-sm-style")])[{i+1}]//div[contains(@class, "sm-collapse")]//div[contains(@class, "sub-link-container")]//a//span[contains(text(), "{link_text}")]', scroll=True)
                assert link_element and link_element.is_displayed(), f'Cannot find {link_text}'
                browser.hover_and_click(link_element)
                logger.info(nav_data[i][link_text])
                verify_url(browser, f'{base_url}{nav_data[i][link_text]}')
            else:
                bottom_links = nav_data[i]['bottom_link'].keys()
                for link_text in bottom_links:
                    browser.activate_page()
                    open_mobile_navbar(browser)
                    open_mobile_dropdown(browser, i, el)
                    link_element = browser.find(xpath=f'(//div[contains(@class, "navlink-sm-style")])[{i+1}]//div[contains(@class, "sm-collapse")]//div[contains(@class, "dropdown-bottom-link")]//a[contains(text(), "{link_text}")]', scroll=True, scroll_by=-200, scroll_to_view='true')
                    assert link_element and link_element.is_displayed(), f'Cannot find {link_text}'
                    browser.hover_and_click(link_element)
                    verify_url(browser, f'{base_url}{nav_data[i]["bottom_link"][link_text]}')

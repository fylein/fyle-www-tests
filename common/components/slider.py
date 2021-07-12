import logging
import time

from .para_blocks import *

logger = logging.getLogger(__name__)


def assert_slider_section(browser):
    side_nav_elements = '//section[contains(@class, "sticky-slider-feature-section")]//ul//li[not(@id="")]'
    list_elements = browser.find_many(xpath=side_nav_elements)
    for i, el in enumerate(list_elements):
        el = browser.find(xpath=f'({side_nav_elements})[{i+1}]')
        browser.hover_and_click(el)
        
        el_id = el.get_attribute('id')
        section_container = browser.find(xpath=f'(//section[contains(@class, "sticky-slider-feature-section")])//div[contains(@class, "slider-image-section-container") and contains(@class, "{el_id}")]')
        time.sleep(2)
        browser_height = browser.get_window_size()['height']
        limit = browser.current_scroll_position()+(browser_height * 0.20)
        assert section_container.location['y'] <= limit, 'Side navigation is not working'

    
def assert_slider_section_para_block(browser, para_width, img_width, spacing):
    assert_para_blocks(browser, para_width, img_width, spacing)

import logging
import time
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta, assert_dimensions, assert_section_spacing

logger = logging.getLogger(__name__)

def assert_h1_spacing(browser, section_class, value=20):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, value)

def assert_bulletin(browser, section_class, spacing_top=None, spacing_bottom=None):
    el = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "last-bulletin")]')
    if spacing_top:
        assert_spacing('top', el, spacing_top)
    if spacing_bottom:
        assert_spacing('bottom', el, spacing_bottom)

def assert_section_spacing(browser, section_class, spacing_top=None, spacing_bottom=None):
    section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]')
    if spacing_top:
        assert_spacing('top', section, spacing_top)
    if spacing_bottom:
        assert_spacing('bottom', section, spacing_bottom)

def assert_hero_img(browser, section_class, img_width):
    hero_image = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "hero-img")]')
    assert hero_image and hero_image.is_displayed(), f'Hero image not displayed in {section_class} page'
    assert_dimensions(hero_image, img_width)

def assert_g2_link(browser, g2_source):
    el = browser.find_by_link_text('Source - G2 Crowd')
    browser.hover_and_click(el)
    browser.switch_tab_next(1)
    assert g2_source in browser.get_current_url(), 'URL is incorrect'
    browser.close_windows()

def assert_demo_button(browser, section_class):
    assert_demo_cta(browser, f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//a[contains(@class, "d-none d-lg-block")]')
    
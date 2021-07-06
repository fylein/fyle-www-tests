import logging
import time
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta, poll_and_assert

logger = logging.getLogger(__name__)

def assert_h1_spacing(browser, section_class, value=20):
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, value)

def assert_subtext_spacing(browser, section_class, value=40):
    span = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "single-column")]//p')
    assert_spacing('bottom', span, value)

def assert_img(browser, img_width, section_class):
    img = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "gradient-hero-img")]')
    assert img and img.is_displayed(), 'Hero image is not displayed'
    assert_element_width(img, img_width)

def assert_button_spacing(browser, section_class, value=40, cta=True):
    button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]'
    if section_class != 'homepage-hero':
        button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]//a'
    button = browser.find(button_xpath)
    assert_spacing('bottom', button, value)
    if cta:
        assert_demo_cta(browser, button_xpath)

def assert_customer_logo(browser, logo_width, section_xpath=None, logo_xpath=None, spacing_top=None, spacing_bottom=None):
    logo_section = browser.find(section_xpath, scroll=True)
    if spacing_top:
        assert_spacing('top', logo_section, spacing_top)
    if spacing_bottom:
        assert_spacing('bottom', logo_section, spacing_bottom)
    
    def check_logo_display():
        logo = browser.find(logo_xpath, scroll=True)
        assert logo and logo.is_displayed(), 'Logo is not displayed'
        assert_element_width(logo, logo_width)

    poll_and_assert(browser, 3, 0.2, check_logo_display)

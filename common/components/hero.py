import logging
import time
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta

logger = logging.getLogger(__name__)

def assert_hero_section(browser, section_class, img_width, logo_width):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, 20)

    #Subtext spacing assertion
    span = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "single-column")]//p')
    assert_spacing('bottom', span, 40)

    #Image assertions
    img = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "gradient-hero-img")]')
    assert img and img.is_displayed(), f'Hero image is not displayed'
    assert_element_width(img, img_width)

    #Customer logo assertions
    customer_logo_section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section', scroll=True)
    assert_spacing('bottom', customer_logo_section, 100)
    assert_spacing('top', customer_logo_section, 100)

    customer_logo = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//img[contains(@class, "hero-customer-logo")]', scroll=True)
    time.sleep(3)
    assert customer_logo and customer_logo.is_displayed(), f'Logo is not displayed'
    assert_element_width(customer_logo, logo_width)

    #Button spacing assertion
    button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]'
    button = browser.find(button_xpath)
    assert_spacing('bottom', button, 40)
    assert_demo_cta(browser, button_xpath)

def assert_mobile_hero_section(browser, section_class):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, 16)

    #Customer logo assertions
    customer_logo_section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section', scroll=True)
    assert_spacing('bottom', customer_logo_section, 50)

    customer_logo = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//div[contains(@class, "d-md-none d-block")]//img[contains(@class, "fy-container-mw-ie")]', scroll=True)
    time.sleep(2)
    assert customer_logo and customer_logo.is_displayed(), f'Logo is not displayed'
    assert_element_width(customer_logo, 375)

    #Button spacing assertion
    button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]'
    button = browser.find(button_xpath)
    assert_spacing('bottom', button, 40)

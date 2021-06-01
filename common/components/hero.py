import logging
import time
from common.asserts import assert_spacing_bottom, assert_element_width, assert_spacing_top

logger = logging.getLogger(__name__)

def assert_hero_section(browser, section_class, img_width, logo_width):
    hero = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]')
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing_bottom(heading, 20)
    span = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "single-column")]//p')
    assert_spacing_bottom(span, 40)
    button = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]')
    assert_spacing_bottom(button, 40)
    img = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "gradient-hero-img")]')
    assert_element_width(img, img_width)
    time.sleep(2)
    customer_logo = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section')
    assert_spacing_bottom(customer_logo, 100)
    assert_spacing_top(customer_logo, 100)

    
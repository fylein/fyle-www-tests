import logging
import time
from common.asserts import assert_element_width, assert_spacing, assert_demo_cta

logger = logging.getLogger(__name__)

def assert_h1_spacing(browser, section_class):
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, 20)

def assert_subtext_spacing(browser, section_class):
    span = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "single-column")]//p')
    assert_spacing('bottom', span, 40)

def assert_img(browser, img_width, section_class):
    img = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "gradient-hero-img")]')
    assert img and img.is_displayed(), 'Hero image is not displayed'
    assert_element_width(img, img_width)

def assert_button_spacing(browser, section_class):
    value = 40
    button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]'
    if section_class != 'homepage-hero':
        value = 48
        button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]//a'
    button = browser.find(button_xpath)
    assert_spacing('bottom', button, value)
    assert_demo_cta(browser, button_xpath)

def assert_customer_logo(browser, section_class, logo_width):
    customer_logo_section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section', scroll=True)
    assert_spacing('bottom', customer_logo_section, 100)
    assert_spacing('top', customer_logo_section, 100)

    customer_logo = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//img[contains(@class, "hero-customer-logo")]', scroll=True)
    time.sleep(3)
    assert customer_logo and customer_logo.is_displayed(), 'Logo is not displayed'
    assert_element_width(customer_logo, logo_width)

def assert_customer_logo_v2(browser, logo_width):
    logo_container = browser.find('//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]', scroll=True)
    assert_spacing('top', logo_container, 80)

    logo = browser.find('//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-block")]', scroll=True)
    time.sleep(3)
    assert logo and logo.is_displayed(), 'Logo is not displayed'
    assert_element_width(logo, logo_width)

def assert_hero_section(browser, section_class, img_width, logo_width):
    #H1 spacing assertions
    assert_h1_spacing(browser, section_class)

    #Subtext spacing assertions
    assert_subtext_spacing(browser, section_class)

    #Image assertions
    assert_img(browser, img_width, section_class)

    #Customer logo assertions
    assert_customer_logo(browser, section_class, logo_width)

    #Button spacing assertion
    assert_button_spacing(browser, section_class)

def assert_mobile_hero_section(browser, section_class):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, 16)

    #Customer logo assertions
    customer_logo_section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section', scroll=True)
    assert_spacing('bottom', customer_logo_section, 50)

    customer_logo = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//section//div[contains(@class, "d-md-none d-block")]//img[contains(@class, "fy-container-mw-ie")]', scroll=True)
    time.sleep(2)
    assert customer_logo and customer_logo.is_displayed(), 'Logo is not displayed'
    assert_element_width(customer_logo, 375)

    #Button spacing assertion
    button_xpath = f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "hero-cta")]'
    button = browser.find(button_xpath)
    assert_spacing('bottom', button, 40)


def assert_product_hero_section(browser, img_width, logo_width, section_class='product-hero'):
    #H1 spacing assertions
    assert_h1_spacing(browser, section_class)

    #Subtext spacing assertions
    assert_subtext_spacing(browser, section_class)

    #Image assertions
    assert_img(browser, img_width, section_class)

    #Customer logo assertions
    assert_customer_logo_v2(browser, logo_width)

    #Button spacing assertion
    assert_button_spacing(browser, section_class)

def assert_product_mobile_hero_section(browser, logo_width, section_class='product-hero'):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    assert_spacing('bottom', heading, 16)

    #Customer logo assertions
    logo_section = browser.find('//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]', scroll=True)
    assert_spacing('top', logo_section, 40)

    customer_logo = browser.find('//section[contains(@class, "customer-logos-v2")]//div[contains(@class, "container")]//img[contains(@class, "d-md-none")]', scroll=True)
    time.sleep(2)
    assert customer_logo and customer_logo.is_displayed(), 'Logo is not displayed'
    assert_element_width(customer_logo, logo_width)

from common.asserts import *

def assert_why_fyle_section(browser, section_spacing, underline_spacing, content_spacing, para_width, img_width, min_img_width=None):
    #Section spacing
    section = browser.find('//section[contains(@class, "fyle-in-map")]', scroll=True)
    assert_spacing('top', section, section_spacing)

    #Spacing check between heading and content
    el = browser.find('//section[contains(@class, "fyle-in-map")]//div[contains(@class, "underline-dash d-none")]', scroll=True, scroll_by=300)
    if underline_spacing:
        assert_spacing('top', el, underline_spacing)
        assert_spacing('bottom', el, underline_spacing)

    #Content spacing
    paras = browser.find_many('//section[contains(@class, "fyle-in-map")]//div[contains(@class, "map-content")]//p')
    assert_spacing('bottom', paras[0], content_spacing)
    for _, el in enumerate(paras):
        assert_element_width(el, para_width)

    #Image width
    img = browser.find('//section[contains(@class, "fyle-in-map")]//div[contains(@class, "map-col")]//img')
    assert_element_width(img, img_width, min_width=min_img_width)

def assert_stat_section(browser, section_spacing, card_width, card_spacing_right, card_spacing_bottom):
    #Section spacing
    section = browser.find('//section[contains(@class, "stat-banner-with-cards")]', scroll=True)
    assert_section_spacing(section, section_spacing, section_spacing)

    #Assert card width and spacing
    cards = browser.find_many('//section[contains(@class, "stat-banner-with-cards")]//div[contains(@class, "benefit-card-col")]')
    for i, el in enumerate(cards):
        if card_width:
            assert_element_width(el, card_width)
        if i != len(cards)-1:
            if card_spacing_right:
                assert_spacing('right', el, card_spacing_right)
            if card_spacing_bottom:
                assert_spacing('bottom', el, card_spacing_bottom)

def assert_fyle_journey(browser, section_spacing, img_xpath, img_width, integration_h2, journey_h2):
    #Section spacing
    section = browser.find('//section[contains(@class, "fyle-journey")]', scroll=True)
    assert_section_spacing(section, section_spacing, section_spacing)

    #Assert img width
    if img_xpath:
        img = browser.find(img_xpath, scroll=True, scroll_by=300)
        assert_element_width(img, img_width)

    #Heading spacing
    h2 = browser.find('//section[contains(@class, "fyle-journey")]//div[contains(@class, "fy-xl-row")]//div[contains(@class, col)]//h2', scroll=True, scroll_by=300)
    assert_spacing('bottom', h2, integration_h2)

    heading = browser.find('//section[contains(@class, "fyle-journey")]//div[contains(@class, "row")]//div[contains(@class, col)]//h2[contains(@class, "feature-section")]', scroll=True, scroll_by=300)
    assert_spacing('bottom', heading, journey_h2)

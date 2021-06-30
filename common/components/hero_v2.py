import logging
from common.asserts import assert_spacing, assert_demo_cta, assert_dimensions, assert_section_spacing
from common.components.hero import assert_customer_logo_v2

logger = logging.getLogger(__name__)

def assert_hero_v2_section(browser, section_class, img_width=None, bulletin=False, section_spacing=None, logo_width=None, g2_source=None):
    #H1 spacing assertion
    heading = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//h1')
    if img_width:
        assert_spacing('bottom', heading, 20)
    else:
        assert_spacing('bottom', heading, 16)

    #Assert bulletin spacing
    if bulletin:
        el = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//div[contains(@class, "last-bulletin")]')
        if img_width:
            assert_spacing('top', el, 30)
        else:
            assert_spacing('top', el, 20)
            assert_spacing('bottom', el, 43)

    #Assert section spacing
    section = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]')
    if section_spacing:
        assert_section_spacing(section, 80, 80)

    if img_width:
        #Assert hero image
        hero_image = browser.find(f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//img[contains(@class, "hero-img")]')
        assert hero_image and hero_image.is_displayed(), f'Hero image not displayed in {section_class} page'
        assert_dimensions(hero_image, img_width)

    #Assert G2 source link
    if g2_source and img_width:
        el = browser.find_by_link_text('Source - G2 Crowd')
        browser.hover_and_click(el)
        browser.switch_tab_next(1)
        assert g2_source in browser.get_current_url(), 'URL is incorrect'
        browser.close_windows()

    if logo_width:
        assert_customer_logo_v2(browser, logo_width)

    if browser.is_desktop():
        assert_demo_cta(browser, f'//section[contains(@class, "gradient-background") and contains(@class, "{section_class}")]//a[contains(@class, "d-none d-lg-block")]')

from time import sleep
import logging

from selenium.common.exceptions import ElementClickInterceptedException

logger = logging.getLogger(__name__)

def assert_thank_you_modal(browser, ty_message, demoform=None):
    e = browser.find(xpath="//div[contains(@id, 'contact-us-ty-modal')]")
    assert e and e.is_displayed, "Thank you modal is not displayed"
    if demoform:
        ty_img = browser.find(xpath="//div[contains(@id, 'contact-us-ty-modal')]//div[contains(@class, 'demo-form-thank-you-img')]")
    else:
        ty_img = browser.find(xpath="//div[contains(@id, 'contact-us-ty-modal')]//div[not(contains(@class, 'demo-form-thank-you-img'))]")
    assert ty_img and ty_img.is_displayed(), "Thank image is not correct"
    ty_text = browser.find(xpath="//div[contains(@id, 'contact-us-ty-modal')]//span[contains(@class, 'ty-box')]").text
    assert ty_text == ty_message, "Thank you message is not correct"

def assert_overflowing(browser):
    assert browser.check_horizontal_overflow(), f'Horizontal Overflow is there in the page {browser.get_current_url()}'

def assert_element_width(element, width, min_width=None):
    element_width = int(element.value_of_css_property('width').replace('px', '').split('.')[0])
    if min_width:
        assert element_width <= width and element_width >= min_width, f"Element width is cincorrect - the expceted value in {width}, and min_width is {min_width}, but {element_width} found"
    else:
        assert element_width == width, f"Element width is incorrect - the expected value is {width}, but {element_width} found"

def verify_url(browser, url):
    assert browser.get_current_url() == url, f"LinkError: The expected URL is {url}, but {browser.get_current_url()} is found"

def get_padding(position, element):
    return int(element.value_of_css_property(f'padding-{position}').replace('px', ''))

def get_margin(position, element):
    return int(element.value_of_css_property(f'margin-{position}').replace('px', ''))

def assert_spacing(position, element, value, assert_msg=None):
    padding = get_padding(position, element)
    margin = get_margin(position, element)
    total_spacing = padding + margin
    msg = f"spacing {position} is not correct, the expected value is {value}, but {total_spacing} found."
    if assert_msg:
        msg = assert_msg
    assert total_spacing == value, msg

def assert_demo_cta(browser, element_path):
    def find_and_click_cta():
        browser.find(element_path, scroll=True, scroll_to_view='false', scroll_by=300)
        browser.click(element_path)
    poll_and_assert(browser, 3, 1, find_and_click_cta, scroll_by=-10)
    form_modal = browser.find(xpath='//div[contains(@class, "modal fade show")]', scroll=True)
    assert form_modal and form_modal.is_displayed(), 'Form modal not displayed, Error in Get a demo CTA'
    sleep(1)
    close_modal(browser)

def close_modal(browser):
    close_btn = browser.find(xpath='//div[contains(@class, "steps-form-modal-body")]//button[contains(@class, "close")]')
    browser.hover_and_click(close_btn)
    exit_intent = browser.find("//div[contains(@class, 'modal fade show') and @id='exit-intent']")
    if exit_intent:
        browser.click('//div[@id="exit-intent"]//button[contains(@class, "close")]')
    form_modal = browser.find(xpath='//div[contains(@class, "modal fade show") contains(@id="demo-form-steps")]', scroll=True)
    assert not form_modal, 'Form modal is not closing'

def verify_url_by_link_text(browser, text, base_url, url, same_tab=False):
    el = browser.find_by_link_text(text, scroll=True, scroll_by=300)
    browser.hover_and_click(el)
    url = f'{base_url}{url}'
    if same_tab:
        verify_url(browser, url)
    else:
        switch_tab_and_verify_url(browser, url)

def switch_tab_and_verify_url(browser, url):
    browser.switch_tab_next(1)
    verify_url(browser, url)
    browser.close_tabs()

def assert_dimensions(element, width=None, height=None):
    if width:
        element_width = int(element.value_of_css_property('width').replace('px', '').split('.')[0])
        assert element_width == width, f"Element width is incorrect - the expected value is {width}, but {element_width} found"
    if height:
        element_height = int(element.value_of_css_property('height').replace('px', '').split('.')[0])
        assert element_height == height, f"Element height is incorrect - the expected value is {height}, but {element_height} found"

def assert_overlap(browser, el):
    try:
        browser.hover_and_click(el)
    except ElementClickInterceptedException as e:
        logger.error(e)
        raise

def assert_section_spacing(el, top, bottom):
    assert_spacing('top', el, top)
    assert_spacing('bottom', el, bottom)

def assert_spacing_all_sides(el, top, right, bottom, left):
    assert_spacing('top', el, top)
    assert_spacing('right', el, right)
    assert_spacing('bottom', el, bottom)
    assert_spacing('left', el, left)

def assert_bottom_banner_cta(browser):
    assert_demo_cta(browser, '//section[contains(@class, "bottom-stat-with-cta")]//a')

def assert_fyle_over_expensify_img_section(browser, width=None, height=None):
    logo = browser.find('//section[contains(@class, "fyle-design-system fy-section-padding")]//img[contains(@class, "d-md-block")]', scroll=True, scroll_by=300)
    assert_dimensions(logo, width, height)
    section = browser.find('//section[contains(@class, "fyle-design-system fy-section-padding")]')
    assert_section_spacing(section, 100, 100)

#max_time and poll_time unit is seconds
def poll_and_assert(browser, max_time, poll_time, func, scroll_by=0):
    no_of_attempts = int(max_time/poll_time)
    for attempt in range(no_of_attempts):
        try:
            func()
        except (Exception, AssertionError) as e:
            if attempt < no_of_attempts-1:
                logger.error(f'Attemp: {attempt} - {e}')
                if scroll_by != 0:
                    browser.scroll_up_or_down(scroll_by)
                sleep(poll_time)
                continue
            else:
                raise
        break

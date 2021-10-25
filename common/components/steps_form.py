from time import sleep
import logging
from math import floor
from selenium.webdriver.common.keys import Keys
from common.asserts import verify_url_by_link_text, assert_spacing, assert_dimensions, poll_and_assert
from common.components.navbar import open_mobile_navbar

logger = logging.getLogger(__name__)

#Open typeform
def open_steps_form(browser):
    def click_on_cta():
        browser.click(xpath="//div[contains(@class, 'nav-item')]//a[contains(text(), 'Get a demo')]")
        assert_steps_form_modal(browser)
    poll_and_assert(browser, 2, 0.5, click_on_cta, scroll_by=10)

def assert_steps_form_modal(browser):
    modal = browser.find(xpath="//div[contains(@class, 'modal fade show')]")
    assert modal and modal.is_displayed, 'Form modal is not opening'

def next_field(browser, count=1, assert_down_arrow=True):
    for _ in range(0, count):
        sleep(0.5)
        down_arrow = browser.click("//div[contains(@class, 'arrow-down-div')]")
        if(assert_down_arrow):
            assert down_arrow and down_arrow.is_displayed(), 'Down navigation button is not working'

def previous_field(browser, count=1):
    for _ in range(0, count):
        sleep(0.5)
        up_arrow = browser.click("//div[contains(@class, 'arrow-up-div')]")
        assert up_arrow and up_arrow.is_displayed(), 'Top navigatin button is not working'

# def get_current_field(browser):
def go_to_email_field(browser):
    for _ in range(0, 6):
        el = browser.find("//div[contains(@class, 'arrow-up-div')]")
        if el:
            return
        else:
            previous_field(browser)


def get_field(browser, field, size=None, consent=None):
    if field == 'email':
        field = browser.find("//div[contains(@class, 'steps-form')]//input[@name='email']")

    if field == 'fullname':
        field = browser.find("//div[contains(@class, 'steps-form')]//input[@name='fullname']")

    if field == 'phone':
        field = browser.find("//div[contains(@class, 'steps-form')]//input[@name='phone']")

    if field == 'company_size':
        field = browser.find(f"//div[contains(@class, 'steps-form')]//label[contains(text(), '{size}')]")

    if field == 'consent':
        field = browser.find(f"//div[contains(@class, 'steps-form')]//label[contains(text(), '{consent}')]")
    return field

def go_to_field(browser, field):
    #First, go to email field and then navigate to the specified field.
    go_to_email_field(browser)

    if field == 'fullname':
        next_field(browser, 1)
        fullname = get_field(browser, 'fullname')
        assert fullname and fullname.is_displayed(), f'Not navigated to {field} field'

    if field == 'phone':
        next_field(browser, 2)
        phone = get_field(browser, 'phone')
        assert phone and phone.is_displayed(), f'Not navigated to {field} field'

    if field == 'company_size':
        next_field(browser, 2)
        next_field(browser, 1, False)
        company_size = get_field(browser, 'company_size', size='>1000')
        assert company_size and company_size.is_displayed(), f'Not navigated to {field} field'


short_cut_keys = {
    'Under 5'  : 1,
    '6 to 25'  : 2,
    '26 to 50' : 3,
    '51 to 100' : 4,
    '101 to 500' : 5,
    '501 to 1000' : 6,
    '>1000' : 7
}

def enter(browser, keys=False):
    button_path = "//div[contains(@class, 'steps-form')]//div[contains(@class, 'next-button')]//button"
    if not keys:
        browser.click(xpath=button_path)
    else:
        button = browser.find(xpath=button_path)
        button.send_keys(Keys.ENTER)

def submit_field(browser, email=None, fullname=None, phone=None, size=None, consent=None, keys=False, submit=True):
    no_of_fields_filled = 0
    if email:
        browser.input(xpath="//div[contains(@class, 'steps-form')]//input[@name='email']", keys=email)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)

    if fullname:
        browser.input(xpath="//div[contains(@class, 'steps-form')]//input[@name='fullname']", keys=fullname)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)

    if phone:
        browser.input(xpath="//div[contains(@class, 'steps-form')]//input[@name='phone']", keys=phone)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser, 1, False)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser, 1, False)

    if size:
        path = f"//div[contains(@class, 'steps-form')]//label[contains(text(), '{size}')]"
        if not keys:
            el = browser.click(xpath=path)
            key_value = short_cut_keys[size]
            radio_btn = browser.find(xpath=f"//div[contains(@class, 'steps-form')]//input[@id='btn-radio-{key_value}']")
            assert el and el.is_displayed() and radio_btn.is_selected(), f'Error in selecting company size {size}'
        else:
            key_value = short_cut_keys[size]
            el = browser.find(xpath=f"//div[contains(@class, 'steps-form')]//input[@id='btn-radio-{key_value}']")
            browser.press_key(f'{key_value}')
            assert el.is_selected(), f'Error in selecting company size {size} by using keys'
        if submit:
            enter(browser, keys=keys)
        else:
            return no_of_fields_filled
        no_of_fields_filled += 1
    else:
        if not submit:
            return no_of_fields_filled;


    enter(browser, keys=keys)
    return no_of_fields_filled


#Assert invalid email
def assert_invalid_email(browser, email='foo'):
    open_steps_form(browser)
    submit_field(browser, email=email)
    e = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='email-error']")
    assert e and e.is_displayed(), 'No error displayed for invalid email'

#Assert required fields
def assert_required_fields(browser):
    open_steps_form(browser)
    enter(browser)
    email_error = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='email-error']")
    assert email_error and email_error.is_displayed(), "No error displayed for missing email"

    next_field(browser)
    enter(browser)
    fullname_error = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='full-name-error']")
    assert fullname_error and fullname_error.is_displayed(), "No error displayed for missing fullname"

    next_field(browser)
    enter(browser)
    phone_error = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='phone-error']")
    assert phone_error and phone_error.is_displayed(), "No error displayed for missing phone number"

    next_field(browser,1, False)
    enter(browser)
    company_size_error = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='company-size-error']")
    assert company_size_error and company_size_error.is_displayed(), "No error displayed for missing company size"

def assert_invalid_phone_number(browser):
    open_steps_form(browser)
    go_to_field(browser, 'phone')
    submit_field(browser, phone='asdf')
    e = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='phone-error']")
    assert e and e.is_displayed(), "No error displayed invalid phone number"
    assert e.get_attribute('innerHTML') == 'Please enter a valid phone number', 'Wrong error message displayed'

def assert_form_success(browser, email='test@fyle.in', fullname='test', phone='898387654', size='501 to 1000', keys=False):
    open_steps_form(browser)
    submit_field(browser, email=email, fullname=fullname, phone=phone, size=size, keys=keys)
    thank_you = browser.find(xpath='//div[contains(@class, "thank-you-typeform")]')
    assert thank_you and thank_you.is_displayed(), 'Thank you message is not displayed'
    sleep(1)
    assert_thank_you_gif(browser)

def close_steps_form(browser, open_form=True):
    if open_form:
        open_steps_form(browser)
    browser.click(xpath='//div[contains(@class, "offer-campaign-dialog")]//button[contains(@class, "close")]')
    exit_intent = browser.find("//div[contains(@class, 'modal fade show') and @id='exit-intent']")
    if exit_intent:
        browser.click('//div[@id="exit-intent"]//button[contains(@class, "close")]')
    modal = browser.find(xpath="//div[contains(@class, 'modal fade show') and @id='demo-form-steps']")
    assert not modal, 'Error in closing form'

def assert_invalid_names(browser):
    open_steps_form(browser)
    go_to_field(browser, 'fullname')
    submit_field(browser, fullname='332fff')
    fullname_error = browser.find(xpath="//div[contains(@class, 'steps-form')]//label[@id='full-name-error']")
    assert fullname_error and fullname_error.is_displayed(), "No error displayed for missing fullname"

def assert_thank_you_gif(browser):
    thank_you_gif = browser.find(xpath='//div[contains(@class, "thank-you-typeform")]//img')
    assert thank_you_gif and thank_you_gif.is_displayed(), "Thank you gif is not displayed"

def assert_logo(browser):
    open_steps_form(browser)
    logos = browser.find_many(xpath='//div[contains(@class, "offer-content")]//img')
    sleep(10)
    for logo in logos:
        assert logo and logo.is_displayed(), 'Logo image not displayed'

def assert_terms_and_conditions_url(browser, base_url):
    open_steps_form(browser)
    submit_field(browser, size='501 to 1000', keys=False, submit=False)
    verify_url_by_link_text(browser, 'terms and conditions', base_url, '/privacy/terms-and-conditions')

def assert_navigation(browser):
    open_steps_form(browser)
    go_to_field(browser, 'company_size')
    go_to_email_field(browser)

def assert_goto_missing_fields(browser, email=None, fullname=None, phone=None, size=None, keys=False):
    open_steps_form(browser)
    submit_field(browser, email=email, fullname=fullname, phone=phone, size=size, keys=keys, submit=False)
    sleep(1)
    if email:
        el = get_field(browser, 'email')
        assert el and el.is_displayed(), 'Not navigated to missing email field on submitting form'
        submit_field(browser, email='test@fyle.in')
    if fullname:
        el = get_field(browser, 'fullname')
        assert el and el.is_displayed(), 'Not navigated to missing fullname field on submitting form'
        submit_field(browser, fullname='test')
    if phone:
        el = get_field(browser, 'phone')
        assert el and el.is_displayed(), 'Not navigated to missing phone field on submitting form'
        enter(browser, keys=keys)
        submit_field(browser, phone='45643231')
    if size:
        el = get_field(browser, 'size', size='>1000')
        assert el and el.is_displayed(), 'Not navigated to missing size field on submitting form'
        enter(browser, keys=keys)
        submit_field(browser, size='>1000')

def assert_values_after_closing_form(browser, email='test@fyle.in', fullname='test', phone='898387654', size='501 to 1000'):
    open_steps_form(browser)
    submit_field(browser, email=email, fullname=fullname, phone=phone, size=size, submit=False)
    close_steps_form(browser, open_form=False)
    open_steps_form(browser)
    email_field = get_field(browser, 'email')
    assert email_field.get_attribute('value') == email, 'Email input value is incorrect or not showing up after form close'
    next_field(browser)

    fullname_field = get_field(browser, 'fullname')
    assert fullname_field.get_attribute('value') == fullname, 'Fullname input value is incorrect or not showing up after form close'
    next_field(browser)

    phone_field = get_field(browser, 'phone')
    assert phone_field.get_attribute('value') == phone, 'Phone number input value is incorrect or not showing up after form close'
    next_field(browser, 1, False)

def assert_progress_bar(browser, email=None, fullname=None, phone=None, size=None, consent=None):
    open_steps_form(browser)
    no_of_fields_filled = submit_field(browser, email=email, fullname=fullname, phone=phone, size=size, consent=consent, submit=False)
    progress_bar_text = browser.find('//div[contains(@class, "form-instance")]//div[contains(@class, "progress-line-bar")]//div[contains(@class, "step-count")]')
    assert progress_bar_text.get_attribute('innerHTML') == f'{no_of_fields_filled} out of 4 answered', 'Progress bar not showing proper values'
    progress_bar = browser.find('//div[contains(@class, "form-instance")]//div[contains(@class, "progress-line-bar")]//div[@id="progress-bar"]')
    progress_bar_width = f'width: {(100/4)*no_of_fields_filled:.4f}%;'
    if no_of_fields_filled == 0:
        progress_bar_width = f'width: {floor((100/4)*no_of_fields_filled)}%;'
    assert progress_bar.get_attribute('style') == progress_bar_width, 'Progress bar not showing proper value'

def assert_thankyou_page_urls(browser, base_url):
    open_steps_form(browser)
    submit_field(browser, email='test@fyle.in', fullname='test', phone='898387654', size='501 to 1000')
    verify_url_by_link_text(browser, 'case studies', base_url, '/resources/case-study')
    verify_url_by_link_text(browser, 'customers love us', base_url, '/customers/reviews')

def assert_firstname_in_phone_field(browser, fullname='test'):
    open_steps_form(browser)
    next_field(browser)
    submit_field(browser, fullname=fullname)
    question_field = browser.find('//div[contains(@class, "phone-block")]//div[contains(@class, "question")]//label[not(@id)]').text
    first_name = question_field.splitlines()[0].split(' ')[-1]
    assert first_name == fullname +'.', 'First name in phone field is incorrect'

def assert_question_spacing(browser, i):
    question_block = browser.find(f'((//div[contains(@class, "block-view")]//div[contains(@class, "question")])[{i+1}]//label)[1]')
    assert_spacing('bottom', question_block, 23)

def assert_number_spacing(browser, i):
    question_number = browser.find(f'(//div[contains(@class, "block-view")]//span[contains(@class, "field-number")])[{i+1}]')
    assert_spacing('right', question_number, 16)

def assert_field_spacing(browser):
    open_steps_form(browser)
    for i in range(2):
        assert_question_spacing(browser, i)
        assert_number_spacing(browser, i)
        next_field(browser)
    next_field(browser, 1, False)
    assert_question_spacing(browser, 3)
    assert_number_spacing(browser, 3)

def assert_radio_pill_spacing(browser, bottom_value=25):
    open_steps_form(browser)
    go_to_field(browser, 'company_size')
    radio_pills = browser.find_many('//label[contains(@class, "radio-pill") and not(contains(@class, "gdpr"))]')
    for pill in radio_pills:
        assert_spacing('right', pill, 25)
        assert_spacing('bottom', pill, bottom_value)


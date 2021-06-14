from time import sleep
from selenium.webdriver.common.keys import Keys
from common.asserts import verify_url_by_link_text
from common.components.navbar import open_mobile_navbar
import logging

logger = logging.getLogger(__name__)

#Open typeform
def open_typeform(browser, nav_open=True):
    if browser.is_desktop():
        browser.click(xpath="//div[contains(@class, 'nav-item')]//a[contains(text(), 'Get a demo')]")
    else:
        if nav_open:
            open_mobile_navbar(browser)
        browser.click(xpath="//a[contains(@class, 'new-contact-us-demo-form')]")

    modal = browser.find(xpath="//div[contains(@class, 'modal fade show')]")
    assert modal and modal.is_displayed, 'Form modal is not opening'

def next_field(browser, count=1):
    for i in range(0, count):
        down_arrow = browser.click("//div[contains(@class, 'up-and-down')]//img[@id='arrow-down']")
        assert down_arrow and down_arrow.is_displayed(), 'Down navigation button is not working'

def previous_field(browser, count=1):
    for i in range(0, count):
        up_arrow = browser.click("//div[contains(@class, 'up-and-down')]//img[@id='arrow-up']")
        assert up_arrow and up_arrow.is_displayed(), 'Top navigatin button is not working'

# def get_current_field(browser):
def go_to_email_field(browser):
    for i in range(0, 6):
        el = browser.find("//div[contains(@class, 'up-and-down')]//img[@id='arrow-up' and contains(@style, 'opacity: 0.7')]")
        if el:
            return
        else:
            previous_field(browser)


def get_field(browser, field, size=None, consent=None):
    if field == 'email':
        field = browser.find("//div[contains(@class, 'typeform')]//input[@name='email']")
    
    if field == 'firstname':
        field = browser.find("//div[contains(@class, 'typeform')]//input[@name='firstname']")
    
    if field == 'lastname':
        field = browser.find("//div[contains(@class, 'typeform')]//input[@name='lastname']")

    if field == 'phone':
        field = browser.find("//div[contains(@class, 'typeform')]//input[@name='phone']")

    if field == 'company_size':
        field = browser.find(f"//div[contains(@class, 'typeform')]//label[contains(text(), '{size}')]")

    if field == 'consent':
        field = browser.find(f"//div[contains(@class, 'typeform')]//label[contains(text(), '{consent}')]")
    return field
    
def go_to_field(browser, field):
    #First, go to email field and then navigate to desired field.
    go_to_email_field(browser)

    if field == 'firstname':
        next_field(browser, 1)
        firstname = get_field(browser, 'firstname')
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'

    if field == 'lastname':
        next_field(browser, 2)
        lastname = get_field(browser, 'lastname')
        assert lastname and lastname.is_displayed(), f'Not navigated to {field} field'

    if field == 'phone':
        next_field(browser, 3)
        phone = get_field(browser, 'phone')
        assert phone and phone.is_displayed(), f'Not navigated to {field} field'

    if field == 'company_size':
        next_field(browser, 4)
        company_size = get_field(browser, 'company_size', size='>1000')
        assert company_size and company_size.is_displayed(), f'Not navigated to {field} field'

    if field == 'consent':
        next_field(browser, 5)
        consent = get_field(browser, 'consent', consent='Yes')
        assert consent and consent.is_displayed(), f'Not navigated to {field} field'


short_cut_map = {
    'Under 5'  : 1,
    '6 to 25'  : 2,
    '26 to 50' : 3,
    '51 to 100' : 4,
    '101 to 500' : 5,
    '501 to 1000' : 6,
    '>1000' : 7
}

def enter(browser, keys=False):
    button_path = "//div[contains(@class, 'typeform')]//div[contains(@class, 'next-button')]//button"
    if not keys:
        browser.click(xpath=button_path)
    else:
        button = browser.find(xpath=button_path)
        button.send_keys(Keys.ENTER)

def submit_field(browser, email=None, firstname=None, lastname=None, phone=None, size=None, consent=None, keys=False, submit=True):
    no_of_fields_filled = 0
    if email:
        #go_to_email_field(browser)
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='email']", keys=email)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)

    if firstname:
        #go_to_field(browser, 'firstname')
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='firstname']", keys=firstname)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)
    if lastname:
        #go_to_field(browser, 'lastname')
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='lastname']", keys=lastname)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)

    if phone:
        #go_to_field(browser, 'phone')
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='phone']", keys=phone)
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)

    if size:
        #go_to_field(browser, 'company_size')
        path = f"//div[contains(@class, 'typeform')]//label[contains(text(), '{size}')]"
        if not keys:
            el = browser.click(xpath=path)
            assert el and el.is_displayed(), f'Error in selecting company size {size}'
        else:
            key_value = short_cut_map[size]
            #el = browser.find(xpath=f"//div[contains(@class, 'typeform')]//input[@id='btnradio{key_value + 1}']")
            browser.press_key(f'{key_value}')
        if submit:
            enter(browser, keys=keys)
        else:
            next_field(browser)
        no_of_fields_filled += 1
    else:
        if not submit:
            next_field(browser)
        
    if consent:
        #go_to_field(browser, 'consent')
        if not keys:
            el = browser.click(xpath=f"//div[contains(@class, 'typeform')]//label[contains(text(), '{consent}')]")
            assert el and el.is_displayed(), f'Error in clicking consent'
        else:
            browser.press_key('y')
        if submit:
            enter(browser, keys=keys)
        no_of_fields_filled += 1

    return no_of_fields_filled
    

#Assert invalid email
def assert_invalid_email(browser, email='foo'):
    open_typeform(browser)
    submit_field(browser, email=email)
    e = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='email-error']")
    assert e and e.is_displayed(), 'No error displayed for invalid email'

#Assert required fields
def assert_required_fields(browser):
    open_typeform(browser)
    enter(browser)
    email_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='email-error']")
    assert email_error and email_error.is_displayed(), "No error displayed for missing email"

    next_field(browser)
    enter(browser)
    firstname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='name-error']")
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for missing firstname"

    next_field(browser)
    enter(browser)
    lastname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='last-name-error']")
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for missing lastname"

    next_field(browser)
    enter(browser)
    phone_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='phone-error']")
    assert phone_error and phone_error.is_displayed(), "No error displayed for missing phone number"

    next_field(browser)
    enter(browser)
    company_size_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='company-size-error']")
    assert company_size_error and company_size_error.is_displayed(), "No error displayed for missing phone number"

    next_field(browser)
    enter(browser)
    consent_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='gdpr-error']")
    assert consent_error and consent_error.is_displayed(), "No error displayed for missing consent"

def assert_invalid_phone_number(browser):
    open_typeform(browser)
    go_to_field(browser, 'phone')
    submit_field(browser, phone='asdf')
    e = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='phone-error']")
    assert e and e.is_displayed(), "No error displayed invalid phone number"
    assert e.get_attribute('innerHTML') == 'Please enter a valid phone number', 'Wrong error message displayed'

def assert_form_success(browser, email='test@fyle.in', firstname='test', lastname='test', phone='898387654', size='501 to 1000', consent='Yes', keys=False):
    open_typeform(browser)
    submit_field(browser, email=email, firstname=firstname, lastname=lastname, phone=phone, size=size, consent=consent, keys=keys)
    thank_you = browser.find(xpath='//div[contains(@class, "thank-you-typeform")]')
    assert thank_you and thank_you.is_displayed(), 'Thank you message is not displayed'

def close_typeform(browser, open_form=True):
    if open_form:
        open_typeform(browser)
    browser.click(xpath='//div[contains(@class, "offer-campaign-dialog")]//button[contains(@class, "close")]')
    modal = browser.find(xpath="//div[contains(@class, 'modal fade show')]")
    assert not modal, 'Error in closing form'

def assert_invalid_names(browser):
    open_typeform(browser)
    go_to_field(browser, 'firstname')
    submit_field(browser, firstname='332fff')
    firstname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='name-error']")
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for missing firstname"

    go_to_field(browser, 'lastname')
    submit_field(browser, lastname='ere4gds')
    lastname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='last-name-error']")
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for missing lastname"

def assert_thank_you_gif(browser):
    assert_form_success(browser)
    thank_you_gif = browser.find(xpath='//div[contains(@class, "thank-you-typeform")]//img')
    thank_you_gif and thank_you_gif.is_displayed(), "Thank you gif is not displayed"

def assert_logo(browser):
    open_typeform(browser)
    logos = browser.find_many(xpath='//div[contains(@class, "offer-content")]//img')
    sleep(10)
    for logo in logos:
        assert logo and logo.is_displayed(), 'Logo image not displayed'

def assert_tc_url(browser, base_url):
    open_typeform(browser)
    go_to_field(browser, 'consent')
    verify_url_by_link_text(browser, 'terms and conditions', base_url, '/privacy/terms-and-conditions')
    
def assert_upward_arrow(browser):
    open_typeform(browser)
    go_to_field(browser, 'consent')
    go_to_email_field(browser)

def assert_downward_arrow(browser):
    open_typeform(browser)
    go_to_field(browser, 'consent')


def assert_goto_missing_fields(browser, email=None, firstname=None, lastname=None, phone=None, size=None, consent=None, keys=False):
    open_typeform(browser)
    submit_field(browser, email=email, firstname=firstname, lastname=lastname, phone=phone, size=size, consent=consent, keys=keys, submit=False)
    enter(browser)
    sleep(1)
    if email == None:
        el = get_field(browser, 'email')
        assert el and el.is_displayed(), f'Not navigated to missing email field on submitting form'
        enter(browser, keys=keys)
    if firstname == None:
        el = get_field(browser, 'firstname')
        assert el and el.is_displayed(), f'Not navigated to missing firstname field on submitting form'
        enter(browser, keys=keys)
    if lastname == None:
        el = get_field(browser, 'lastname')
        assert el and el.is_displayed(), f'Not navigated to missing lastname field on submitting form'
        enter(browser, keys=keys)
    if phone == None:
        el = get_field(browser, 'phone')
        assert el and el.is_displayed(), f'Not navigated to missing phone field on submitting form'
        enter(browser, keys=keys)
    if size == None:
        el = get_field(browser, 'size')
        assert el and el.is_displayed(), f'Not navigated to missing size field on submitting form'
        enter(browser, keys=keys)
    if consent == None:
        el = get_field(browser, 'consent')
        assert el and el.is_displayed(), f'Not navigated to missing consent field on submitting form'
        enter(browser, keys=keys)

def assert_values_after_closing_form(browser, email='test@fyle.in', firstname='test', lastname='test', phone='898387654', size='501 to 1000', consent='Yes'):
    open_typeform(browser)
    submit_field(browser, email=email, firstname=firstname, lastname=lastname, phone=phone, size=size, consent=consent, submit=False)
    close_typeform(browser, open_form=False)
    open_typeform(browser, nav_open=False)
    email_field = get_field(browser, 'email')
    assert email_field.get_attribute('value') == email, 'Email input value is incorrect or not showing up after form close'
    next_field(browser)

    firstname_field = get_field(browser, 'firstname')
    assert firstname_field.get_attribute('value') == firstname, 'Firstname input value is incorrect or not showing up after form close'
    next_field(browser)

    lastname_field = get_field(browser, 'lastname')
    assert lastname_field.get_attribute('value') == lastname, 'Lastname input value is incorrect or not showing up after form close'
    next_field(browser)

    phone_field = get_field(browser, 'phone')
    assert phone_field.get_attribute('value') == phone, 'Phone number input value is incorrect or not showing up after form close'
    next_field(browser)

def assert_progress_bar(browser):
    open_typeform(browser)
    no_of_fields_filled = submit_field(browser, email='test@fyle.in', firstname='test', size='501 to 1000', consent='Yes')
    progress_bar_text = browser.find('//div[contains(@class, "form-instance")]//div[contains(@class, "progress-line-bar")]//div[contains(@class, "step-count")]')
    assert progress_bar_text.get_attribute('innerHTML') == f'{no_of_fields_filled} out of 6 answered', 'Progress bar not showing proper values'
    progress_bar_width = browser.find('//div[contains(@class, "form-instance")]//div[contains(@class, "progress-line-bar")]//div[@id="progress-bar"]')
    assert progress_bar_width.get_attribute('style') == f'width: {(100/6)*no_of_fields_filled:.4f}%;'
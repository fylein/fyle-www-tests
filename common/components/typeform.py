from time import sleep
from selenium.webdriver.common.keys import Keys
from common.asserts import verify_url_by_link_text
import logging

logger = logging.getLogger(__name__)

#Open typeform
def open_typeform(browser):
    if browser.is_desktop():
        browser.click(xpath="//div[contains(@class, 'nav-item')]//a[contains(text(), 'Get a demo')]")
    else:
        browser.click(xpath="//div[contains(@class, 'sticky-cta-mobile')]/a")

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
def got_to_email_field(browser):
    el = browser.find("//div[contains(@class, 'up-and-down')]//img[@id='arrow-up' and contains(@style, 'opacity: 0.7')]")
    if el:
        return
    else:
        previous_field(browser)
        got_to_email_field(browser)
    
def go_to_field(browser, field):
    #First, go to email field and then navigate to desired field.
    got_to_email_field(browser)

    if field == 'firstname':
        next_field(browser, 1)
        firstname = browser.find("//div[contains(@class, 'typeform')]//input[@name='firstname']")
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'

    if field == 'lastname':
        next_field(browser, 2)
        firstname = browser.find("//div[contains(@class, 'typeform')]//input[@name='lastname']")
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'

    if field == 'phone':
        next_field(browser, 3)
        firstname = browser.find("//div[contains(@class, 'typeform')]//input[@name='phone']")
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'

    if field == 'company_size':
        next_field(browser, 4)
        firstname = browser.find("//div[contains(@class, 'typeform')]//label[contains(text(), '>2500')]")
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'

    if field == 'consent':
        next_field(browser, 5)
        firstname = browser.find("//div[contains(@class, 'typeform')]//label[contains(text(), 'Yes')]")
        assert firstname and firstname.is_displayed(), f'Not navigated to {field} field'


short_cut_map = {
    'Under 5'  : 1,
    '6 to 25'  : 2,
    '26 to 50' : 3,
    '51 to 100' : 4,
    '101 to 500' : 5,
    '501 to 1000' : 6,
    '>1000' : 7
}

def submit_field(browser, email=None, firstname=None, lastname=None, phone=None, size=None, consent=None, keys=False):
    if email:
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='email']", keys=email)
    if firstname:
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='firstname']", keys=firstname)
    if lastname:
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='lastname']", keys=lastname)
    if phone:
        browser.input(xpath="//div[contains(@class, 'typeform')]//input[@name='phone']", keys=phone)
    if size:
        path = f"//div[contains(@class, 'typeform')]//label[contains(text(), '{size}')]"
        if not keys:
            el = browser.click(xpath=path)
            assert el and el.is_displayed(), f'Error in selecting company size {size}'
        else:
            key_value = short_cut_map[size]
            #el = browser.find(xpath=f"//div[contains(@class, 'typeform')]//input[@id='btnradio{key_value + 1}']")
            browser.press_key(f'{key_value}')
        
    if consent:
        if not keys:
            el = browser.click(xpath=f"//div[contains(@class, 'typeform')]//label[contains(text(), '{consent}')]")
            assert el and el.is_displayed(), f'Error in clicking consent'
        else:
            browser.press_key('y')

    #submit form by click
    button_path = "//div[contains(@class, 'typeform')]//div[contains(@class, 'next-button')]//button"
    if not keys:
        browser.click(xpath=button_path)
    else:
        button = browser.find(xpath=button_path)
        button.send_keys(Keys.ENTER)


#Assert invalid email
def assert_invalid_email(browser, email='foo'):
    open_typeform(browser)
    submit_field(browser, email=email)
    e = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='email-error']")
    assert e and e.is_displayed(), 'No error displayed for invalid email'

#Assert required fields
def assert_required_fields(browser):
    open_typeform(browser)
    submit_field(browser)
    email_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='email-error']")
    assert email_error and email_error.is_displayed(), "No error displayed for missing email"

    next_field(browser)
    submit_field(browser)
    firstname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='name-error']")
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for missing firstname"

    next_field(browser)
    submit_field(browser)
    lastname_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='last-name-error']")
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for missing lastname"

    next_field(browser)
    submit_field(browser)
    phone_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='phone-error']")
    assert phone_error and phone_error.is_displayed(), "No error displayed for missing phone number"

    next_field(browser)
    submit_field(browser)
    company_size_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='company-size-error']")
    assert company_size_error and company_size_error.is_displayed(), "No error displayed for missing phone number"

    next_field(browser)
    submit_field(browser)
    consent_error = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='gdpr-error']")
    assert consent_error and consent_error.is_displayed(), "No error displayed for missing consent"

def assert_invalid_phone_number(browser):
    open_typeform(browser)
    go_to_field(browser, 'phone')
    submit_field(browser, phone='asdf')
    e = browser.find(xpath="//div[contains(@class, 'typeform')]//label[@id='phone-error']")
    assert e and e.is_displayed(), "No error displayed invalid phone number"
    assert e.get_attribute('innerHTML') == 'Please enter a valid phone number', 'Wrong error message displayed'

def assert_form_success(browser, keys=False):
    open_typeform(browser)
    submit_field(browser, email='test@fyle.in', keys=keys)

    #sleep(1)
    submit_field(browser, firstname='test', keys=keys)

    #sleep(1)
    submit_field(browser, lastname='test', keys=keys)

    #sleep(1)
    submit_field(browser, phone='898387654', keys=keys)

    #sleep(1)
    submit_field(browser, size='501 to 1000', keys=keys)

    #sleep(1)
    submit_field(browser, consent='Yes', keys=keys)

    thank_you = browser.find(xpath='//div[contains(@class, "thank-you-typeform")]')
    assert thank_you and thank_you.is_displayed(), 'Thank you message is not displayed'

def close_typeform(browser):
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
    sleep(3)
    for logo in logos:
        assert logo and logo.is_displayed(), 'Logo image not displayed'

def assert_tc_url(browser, base_url):
    open_typeform(browser)
    go_to_field(browser, 'consent')
    verify_url_by_link_text(browser, 'terms and conditions', base_url, '/privacy/terms-and-conditions')
    
def assert_upward_arrow(browser):
    open_typeform(browser)
    go_to_field(browser, 'consent')
    got_to_email_field(browser)

def assert_downward_arrow(browser):
    open_typeform(browser)
    go_to_field(browser, 'consent')
from time import sleep
import logging
from common.asserts import assert_thank_you_modal

logger = logging.getLogger(__name__)

def open_getdemo_form(browser):
    if browser.is_desktop():
        browser.click(xpath="//div[contains(@class, 'nav-item')]//a[contains(text(), 'Get a demo')]")
    else:
        browser.click(xpath="//div[contains(@class, 'sticky-cta-mobile')]/a")

def submit_getdemo_form(browser, email=None, firstname=None, lastname=None, phone=None, company_size=None, agree=None, modal=''):
    if email:
        browser.input(xpath=f"//input[@id='demo-email{modal}']", keys=email)
    if firstname:
        browser.input(xpath=f"//form[@id='contact-us-form{modal}']//input[@name='firstname']", keys=firstname)
    if lastname:
        browser.input(xpath=f"//form[@id='contact-us-form{modal}']//input[@name='lastname']", keys=lastname)
    if phone:
        browser.input(xpath=f"//form[@id='contact-us-form{modal}']//input[@name='phone']", keys=phone)
    if company_size:
        browser.click(xpath=f"//form[@id='contact-us-form{modal}']//input[@id='number_of_employees{modal}']")
        browser.click(xpath=f"//form[@id='contact-us-form{modal}']//li[@value='{company_size}']")
    if agree:
        browser.click(xpath=f'//form[@id="contact-us-form{modal}"]//div[contains(@class, "custom-checkbox")]')
    browser.click(xpath=f'//form[@id="contact-us-form{modal}"]//button[text()=" Get a demo "]')

def assert_bad_email(browser, email='foo', inline=False):
    modal = '-outside-modal'
    if not inline:
        open_getdemo_form(browser)
        modal = ''
    submit_getdemo_form(browser, email=email, modal=modal)
    e = browser.find(xpath=f"//form[@id='contact-us-form{modal}']//label[@for='demo-email{modal}'][@class='error']")
    assert e and e.is_displayed(), 'No error displayed for invalid email'

def assert_required_fields(browser, inline=False):
    modal = '-outside-modal'
    if not inline:
        open_getdemo_form(browser)
        modal = ''
    submit_getdemo_form(browser, modal=modal)
    email_error = browser.find(xpath=f"//label[@for='demo-email{modal}'][@class='error']")
    firstname_error = browser.find(xpath=f"//label[@for='demo-first-name{modal}'][@class='error demo-first-name-error']")
    lastname_error = browser.find(xpath=f"//label[@for='demo-last-name{modal}'][@class='error demo-last-name-error']")
    company_size_error = browser.find(xpath=f"//label[@for='number_of_employees{modal}'][@class='error']")
    consent_error = browser.find(xpath=f"//form[@id='contact-us-form{modal}']//label[@for='gdpr_consent'][@class='error']")
    assert email_error and email_error.is_displayed(), "No error displayed for missing email"
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for missing firstname"
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for missing lastname"
    assert company_size_error and company_size_error.is_displayed(), "No error displayed for missing company size"
    assert consent_error and consent_error.is_displayed(), "No error displayed for missing checkbox"

def assert_success(browser, email='test@fyle.in', firstname='test', lastname='test', phone='123456789', company_size='Under 5', agree=True, inline=False):
    modal = '-outside-modal'
    if not inline:
        open_getdemo_form(browser)
        modal = ''
    submit_getdemo_form(browser, email=email, firstname=firstname, lastname=lastname, phone=phone, company_size=company_size, agree=agree, modal=modal)
    e = browser.find(xpath="//h3[contains(text(), 'Thank')]")
    sleep(2)
    assert e and e.is_displayed(), 'Not displaying thank you message'
    ty_message = 'Our sales team will respond within the next 60 minutes to schedule a detailed product demo.'
    assert_thank_you_modal(browser, ty_message, 'demoform')

def assert_non_business_email(browser, email='test@gmail.com', firstname='test', lastname='test', phone='1234567865', company_size='Under 5', agree=True, inline=False):
    modal = '-outside-modal'
    if not inline:
        open_getdemo_form(browser)
        modal = ''
    submit_getdemo_form(browser, email=email, firstname=firstname, lastname=lastname, phone=phone, company_size=company_size, agree=agree, modal=modal)
    sleep(2)
    email_error = browser.find(xpath=f"//label[@for='demo-email{modal}'][@class='error email-error']")
    assert email_error and email_error.is_displayed(), 'No error displayed for non business email'

def assert_invalid_names(browser, first_name='test1', last_name='test2', inline=False):
    modal = '-outside-modal'
    if not inline:
        open_getdemo_form(browser)
        modal = ''
    submit_getdemo_form(browser, firstname=first_name, lastname=last_name, modal=modal)
    firstname_error = browser.find(xpath=f"//label[@for='demo-first-name{modal}'][@class='error demo-first-name-error']")
    lastname_error = browser.find(xpath=f"//label[@for='demo-last-name{modal}'][@class='error demo-last-name-error']")
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for invalid firstname"
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for invalid lastname"

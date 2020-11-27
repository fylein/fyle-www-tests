import logging
from common.asserts import assert_thank_you_modal

logger = logging.getLogger(__name__)

def open_getdemo_form(browser):
    if browser.is_desktop():
        browser.click(xpath="//div[contains(@class, 'nav-item')]//a[contains(text(), 'Get a demo')]")
    else:
        browser.click(xpath="//div[contains(@class, 'sticky-cta-mobile')]/a")

def submit_getdemo_form(browser, email=None, firstname=None, lastname=None, phone=None, company_size=None, agree=None):
    if email:
        browser.input(xpath="//input[@name='email']", keys=email)
    if firstname:
        browser.input(xpath="//input[@name='firstname']", keys=firstname)
    if lastname:
        browser.input(xpath="//input[@name='lastname']", keys=lastname)
    if phone:
        browser.input(xpath="//input[@name='phone']", keys=phone)
    if company_size:
        browser.click(xpath="//input[@id='number_of_employees']")
        browser.click(xpath=f"//form[@id='contact-us-form']//li[@value='{company_size}']")
    if agree:
        browser.click(xpath='//div[contains(@class, "custom-checkbox")]')
    browser.click(xpath='//button[text()=" Get a demo "]')

def assert_bad_email(browser):
    open_getdemo_form(browser)
    submit_getdemo_form(browser, email='foo')
    e = browser.find(xpath="//form[@id='contact-us-form']//label[@for='demo-email'][@class='error']")
    assert e and e.is_displayed(), 'No error displayed for invalid email'

def assert_required_fields(browser):
    open_getdemo_form(browser)
    submit_getdemo_form(browser)
    email_error = browser.find(xpath="//label[@for='demo-email'][@class='error']")
    firstname_error = browser.find(xpath="//label[@for='demo-first-name'][@class='error demo-first-name-error']")
    lastname_error = browser.find(xpath="//label[@for='demo-last-name'][@class='error demo-last-name-error']")
    company_size_error = browser.find(xpath="//label[@for='number_of_employees'][@class='error']")
    consent_error = browser.find(xpath="//label[@for='gdpr_consent'][@class='error']")
    assert email_error and email_error.is_displayed(), "No error displayed for missing email"
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for missing firstname"
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for missing lastname"
    assert company_size_error and company_size_error.is_displayed(), "No error displayed for missing company size"
    assert consent_error and consent_error.is_displayed(), "No error displayed for missing checkbox"

def assert_success(browser):
    open_getdemo_form(browser)
    submit_getdemo_form(browser, email='test@fyle.in', firstname='test', lastname='test', phone='123456789', company_size='Under 5', agree=True)
    e = browser.find(xpath="//h3[contains(text(), 'Thank')]")
    assert e and e.is_displayed(), 'Not displaying thank you message'
    ty_message = 'Sit back and relax. Our Sales team will get in touch with you within the next 24 hours to schedule a detailed demo.'
    assert_thank_you_modal(browser, ty_message, 'demoform')

def assert_non_business_email(browser):
    open_getdemo_form(browser)
    submit_getdemo_form(browser, email='test@gmail.com', firstname='test', lastname='test', phone='1234567865', company_size='Under 5', agree=True)
    email_error = browser.find(xpath="//label[@for='demo-email'][@class='error email-error']")
    assert email_error and email_error.is_displayed(), 'No error displayed for non business email'

def assert_invalid_names(browser):
    open_getdemo_form(browser)
    submit_getdemo_form(browser, firstname='test1', lastname='test2')
    firstname_error = browser.find(xpath="//label[@for='demo-first-name'][@class='error demo-first-name-error']")
    lastname_error = browser.find(xpath="//label[@for='demo-last-name'][@class='error demo-last-name-error']")
    assert firstname_error and firstname_error.is_displayed(), "No error displayed for invalid firstname"
    assert lastname_error and lastname_error.is_displayed(), "No error displayed for invalid lastname"

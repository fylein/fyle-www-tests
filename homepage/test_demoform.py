import logging
from common.test_getdemo import assert_bad_email, assert_required_fields, assert_non_business_email, assert_invalid_names

logger = logging.getLogger(__name__)

#Check demo form (common section)
def test_bad_email(browser):
    assert_bad_email(browser)

def test_required_fields(browser):
    assert_required_fields(browser)

def test_non_business_email(browser):
    assert_non_business_email(browser=browser)

def test_invalid_names(browser):
    assert_invalid_names(browser=browser)

import pytest
from common.utils import resize_browser

# from common.components.demo_form import DemoForm
def init_browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/expense-report-software')
    site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
    module_browser.hover(site_element)
    return module_browser

#Desktop - 1920px
@pytest.fixture(params=[('desktop_1')], scope='function')
def desktop_browser(module_browser, base_url, request):
    return init_browser(module_browser, base_url, request)

#Laptop - 1440px
@pytest.fixture(params=[('laptop_1')], scope='function')
def laptop_browser(module_browser, base_url, request):
    return init_browser(module_browser, base_url, request)

#Mobile - 441px
@pytest.fixture(params=[('mobile_1')], scope='function')
def mobile_browser(module_browser_mobile, base_url, request):
    return init_browser(module_browser_mobile, base_url, request)

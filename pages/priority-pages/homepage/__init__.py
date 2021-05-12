import pytest
from common.utils import resize_browser
# from common.components.demo_form import DemoForm
def init_browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/')
    site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
    module_browser.hover(site_element)
    return module_browser

#Desktop - 1920
@pytest.fixture(params=[('desktop_1')], scope='function')
def desktop_browser(module_browser, base_url, request):
    return init_browser(module_browser, base_url, request)

#Mobile - 445
@pytest.fixture(params=[('mobile_1')], scope='function')
def mobile_browser(module_browser, base_url, request):
    return init_browser(module_browser, base_url, request)

#Laptop - 1440
#......Code for Other resolutions
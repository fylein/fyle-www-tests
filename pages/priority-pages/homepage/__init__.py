import pytest
from common.utils import resize_browser
# from common.components.demo_form import DemoForm

@pytest.fixture(params=[('desktop_1')], scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/')
    #time.sleep(4)
    site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
    module_browser.hover(site_element)
    return module_browser

# Form = DemoForm()
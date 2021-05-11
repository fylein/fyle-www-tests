import time
import logging
import pytest

from common.utils import resize_browser
from common.components.para_blocks import assert_para_blocks

logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def browser(module_browser, base_url, request):
    resize_browser(browser=module_browser, resolution=request.param)
    module_browser.get(base_url + '/solutions/goals/project-spends')
    #time.sleep(4)
    site_element = module_browser.find(xpath='//div[contains(@class, "site-content")]')
    module_browser.hover(site_element)
    return module_browser

@pytest.mark.parametrize('browser', [('desktop_1')], indirect=True)
def test_para_blocks(browser):
    assert_para_blocks(browser)

import os
import logging
from simplebrowser import SimpleBrowser

logger = logging.getLogger(__name__)

resolutions = {
    'desktop_1': {'width': 1920, 'height': 864},
    'laptop_1' : {'width': 1440, 'height': 864},
    'mobile_1': {'width': 500, 'height': 896}
}

def get_resolution(browser):
    for res, value in resolutions.items():
        if value == browser.get_window_size():
            return res

def get_browser_name():
    return os.getenv('BROWSER', 'chrome')

def create_browser(browser_name, capabilities):
    browser = SimpleBrowser(browser_name, capabilities)
    return browser

def resize_browser(browser, resolution):
    width = resolutions[resolution]['width']
    height = resolutions[resolution]['height']
    browser.set_window_size(width=width, height=height)
    return browser

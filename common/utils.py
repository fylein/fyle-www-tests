import logging
import os

from simplebrowser import SimpleBrowser

logger = logging.getLogger(__name__)

resolutions = {
    'desktop_1': {'width': 1920, 'height': 864},
    'mobile_1': {'width': 414, 'height': 896}
}

def create_browser():
    name = os.getenv('BROWSER', 'chrome')
    browser = SimpleBrowser(browser=name)
    return browser

def resize_browser(browser, resolution):
    width = resolutions[resolution]['width']
    height = resolutions[resolution]['height']
    browser.set_window_size(width=width, height=height)
    return browser

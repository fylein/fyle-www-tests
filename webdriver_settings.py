from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

import os
import logging

logger = logging.getLogger(__name__)

def get_driver(browser, capabilities, emulation):
    if browser == 'chrome':
        if emulation:
            emulation_options = {
                "deviceMetrics": { "width": 414, "height": 812, "pixelRatio": 3.0 },
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
            }
            chrome_options = Options()
            chrome_options.add_experimental_option("mobileEmulation", emulation_options)
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    if browser == 'safari':
        driver = webdriver.Safari()
    if browser == 'remote':
        user_name = os.getenv('LAMBDA_USER_NAME', None)
        access_key = os.getenv('LAMBDA_ACCESS_KEY', None)

        driver = webdriver.Remote(
            command_executor= f'https://{user_name}:{access_key}@hub.lambdatest.com/wd/hub',
            desired_capabilities= capabilities
        )
    
    return driver

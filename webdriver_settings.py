from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

import os
import logging

logger = logging.getLogger(__name__)

def get_driver(browser, capabilities):
    if browser == 'chrome':
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

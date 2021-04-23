from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import logging

logger = logging.getLogger(__name__)

def get_driver(browser):
    driver = None

    if browser == 'chrome' or None:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    if browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
    # if browser == 'edge':
    #   driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    if browser == 'remote':
        user_name = os.getenv('LAMBDA_USER_NAME', None)
        access_key = os.getenv('LAMBDA_ACCESS_KEY', None)

        driver = webdriver.Remote(
            command_executor= f'https://{user_name}:{access_key}@hub.lambdatest.com/wd/hub',
            desired_capabilities= {
                "build" : "Website Form",
                "name" : "Bad email",
                "platform" : "Windows 10",
                "browserName" : "Chrome",
                "version" : "88.0",
                "console" : True,
                "implicit_wait" : 8,
            }
        )

    return driver

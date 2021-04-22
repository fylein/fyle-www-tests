from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser):
  driver = None

  if browser == 'chrome' or None:
    driver = webdriver.Chrome(ChromeDriverManager().install())
  if browser == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
  if browser == 'ie':
    driver = webdriver.Ie(IEDriverManager().install(), options=options)
  # if browser == 'edge':
  #   driver = webdriver.Edge(EdgeChromiumDriverManager().install())

  return driver

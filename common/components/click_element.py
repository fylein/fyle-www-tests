import logging
logger = logging.getLogger(__name__)
# browser = browser()

def click(browser, text):
  xpath=f'(//span[contains(text(), "{text}")]//..)'
  element = browser.find(xpath, scroll=True)
  assert element, 'Unable to find element'
  logger.info(element)
  ele = browser.hover_and_click(element)
  assert ele, 'Unable to click on element'
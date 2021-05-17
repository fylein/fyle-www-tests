import logging
logger = logging.getLogger(__name__)

def find(browser, text):
  logger.info(browser)
  xpath = f'//h2[contains(text(), "{text}")]'
  ele = browser.find(xpath=xpath, scroll=True)
  logger.info(ele)
  assert ele, 'Unable to find an element'
  if ele:
    return ele
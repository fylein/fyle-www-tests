import time
import logging

from common.asserts import assert_spacing_left, assert_spacing_right

logger = logging.getLogger(__name__)

def assert_para_blocks(browser):
  left_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-left-para-padding')]")
  right_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-right-para-padding')]")
  assert_left_right_spacing(left_blocks, right_blocks, 85)

def assert_left_right_spacing(left_blocks, right_blocks, value):
    for i, left_block in enumerate(left_blocks):
        assert_spacing_right(left_block, value)
        logger.info(i)
    for i, right_block in enumerate(right_blocks):
        assert_spacing_left(right_block, value)
        logger.info(i)
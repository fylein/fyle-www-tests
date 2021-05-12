import time
import logging

from common.asserts import assert_spacing_left, assert_spacing_right, assert_element_width

logger = logging.getLogger(__name__)

def assert_para_blocks(browser, para_width, image_width, spacing=0):
    left_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-left-para-padding')]")
    right_blocks = browser.find_many(xpath="//section[contains(@class, 'features-parallel-content-img')]//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-right-para-padding')]")

    for i, left_block in enumerate(left_blocks):
        assert_spacing_right(left_block, value)
        assert_element_width(left_block, para_width)
        # assert_image_width(left_block, image_width)
        #logger.info(i)
    for i, right_block in enumerate(right_blocks):
        assert_spacing_left(right_block, value)
        assert_element_width(left_block, para_width)
        # assert_image_width(left_block, image_width)
        #logger.info(i)


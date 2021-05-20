import time
import logging

from common.asserts import assert_spacing_left, assert_spacing_right, assert_element_width

logger = logging.getLogger(__name__)

def assert_para_blocks(browser, para_width, image_width, spacing=0):
    left_blocks = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-left-para-padding')]")
    right_blocks = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-right-para-padding')]")
    right_block_videos = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=1]//video")
    left_block_vidoes = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=2]//video")

    for i, left_block in enumerate(left_blocks):
        assert_spacing_right(left_block, spacing)
        assert_element_width(left_block, para_width)
        if i < (len(left_blocks) - len(left_block_vidoes)):
            left_block_image = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=2]//img)[{i+1}]", scroll=True)
            time.sleep(4)
            assert_element_width(left_block_image, image_width)

    for i, right_block in enumerate(right_blocks):
        assert_spacing_left(right_block, spacing)
        assert_element_width(right_block, para_width)
        if i <= (len(right_blocks) - len(right_block_videos)):
            right_block_image = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=1]//img)[{i+1}]", scroll=True)
            time.sleep(4)
            assert_element_width(right_block_image, image_width)

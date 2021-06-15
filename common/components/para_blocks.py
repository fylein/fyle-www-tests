import time
import logging

from common.asserts import assert_element_width, assert_spacing

logger = logging.getLogger(__name__)

def assert_para_blocks(browser, para_width, image_width, spacing=None):
    left_blocks = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-left-para-padding')]")
    right_blocks = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'fy-feature-right-para-padding')]")
    right_block_videos = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=1]//video")
    left_block_vidoes = browser.find_many(xpath="//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=2]//video")

    for i, left_block in enumerate(left_blocks):
        if spacing != None:
            assert_spacing('right', left_block, spacing)
        assert_element_width(left_block, para_width, min_width=(para_width-20))
        left_block_el = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=2 and not(contains(@class, 'fy-feature-right-para-padding'))])[{i+1}]//img", scroll=True, scroll_to_view='true')
        if left_block_el == False:
            left_block_el = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=2 and not(contains(@class, 'fy-feature-right-para-padding'))])[{i+1}]//video", scroll=True, scroll_to_view='true')
        time.sleep(5)
        assert_element_width(left_block_el, image_width, min_width=(image_width-20))

    for i, right_block in enumerate(right_blocks):
        if spacing != None:
            assert_spacing('left', right_block, spacing)
        assert_element_width(right_block, para_width, min_width=(para_width-20))
        right_block_el = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=1 and not(contains(@class, 'fy-feature-left-para-padding'))])[{i+1}]//img", scroll=True, scroll_to_view='true')
        if right_block_el == False:
            right_block_el = browser.find(xpath=f"(//div[contains(@class, 'fyle-features-row')]//div[contains(@class, 'col') and position()=1 and not(contains(@class, 'fy-feature-left-para-padding'))])[{i+1}]//video", scroll=True, scroll_to_view='true')
        time.sleep(5)
        assert_element_width(right_block_el, image_width, min_width=(image_width-20))
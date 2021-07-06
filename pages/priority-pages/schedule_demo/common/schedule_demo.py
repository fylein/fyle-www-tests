from common.asserts import *

def assert_demo_section(browser, list_bottom_spacing=15, last_list_spacing=34):
    h1 = browser.find('//section[contains(@class, "schedule-demo")]//h1')
    assert_spacing('bottom', h1, 10)

    span = browser.find('//div[contains(@class, "schedule-demo")]//p')
    assert_spacing('bottom', span, 20)

    lists = browser.find_many('//div[contains(@class, "schedule-demo")]//li')
    for i, li in enumerate(lists):
        assert_spacing('left', li, 20)
        if i != len(lists)-1:
            assert_spacing('bottom', li, list_bottom_spacing)
        else:
            assert_spacing('bottom', li, last_list_spacing)

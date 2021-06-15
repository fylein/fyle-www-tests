import logging
import random
from time import sleep
import json

from selenium.common.exceptions import SessionNotCreatedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_settings import get_driver

logger = logging.getLogger(__name__)


class SimpleBrowser:

    @classmethod
    def __create_driver(cls, browser, capabilities):
        assert browser in ['chrome', 'ie', 'edge', 'safari',
                           'firefox', 'remote', None], 'unsupported browser'
        driver = None
        for _ in range(0, 3):
            try:
                #Getting driver from webdriver_settings
                driver = get_driver(browser, capabilities)
            except SessionNotCreatedException:
                logger.exception('couldnt create session properly')
                sleep(4)
            if driver:
                break
        return driver

    def __init__(self, browser, capabilities):
        self.browser = browser
        self.driver = SimpleBrowser.__create_driver(browser=browser, capabilities=capabilities)
        assert self.driver, 'unable to initialize browser properly'
        self.timeout = 5
        self.wait = WebDriverWait(self.driver, self.timeout)

    def quit(self):
        sleep(1)
        driver = self.driver
        self.driver = None
        if driver:
            driver.quit()
        #sleep(2)
    
    def close(self):
        sleep(1)
        driver = self.driver
        self.driver = None
        if driver:
            driver.close()

    def __del__(self):
        logger.debug('destructor called')
        self.quit()

    def get(self, url):
        return self.driver.get(url)

    def checkbox_click(self, elem):
        self.driver.execute_script("arguments[0].click();", elem)

    def current_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def current_scroll_position(self):
        return self.driver.execute_script("return window.pageYOffset")

    def scroll_down_page(self, max_speed=300):
        current_scroll_position = 0
        new_height = 1
        while current_scroll_position <= new_height:
            delta = random.randint(1, max_speed)
            current_scroll_position += delta
            self.driver.execute_script(f'window.scrollTo(0, {current_scroll_position});')
            sleep(random.uniform(0.0, 1.0))
            new_height = self.current_height()

    def scroll_up_page(self, max_speed=300):
        pos = self.current_scroll_position()
        while pos > 0:
            delta = random.randint(1, max_speed)
            pos -= delta
            if pos < 0:
                pos = 0
            self.driver.execute_script(f'window.scrollTo(0, {pos});')
            sleep(random.uniform(0.0, 1.0))

    def scroll_up_or_down(self, pixels_to_scroll):
        self.driver.execute_script(f'window.scrollBy(0, {pixels_to_scroll});')
        sleep(random.uniform(0.0, 1.0))

    def find(self, xpath, scroll=False, scroll_by=0, scroll_to_view='false'):
        try:
            l = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if scroll:
                self.driver.execute_script(f"arguments[0].scrollIntoView({scroll_to_view});", l)
                sleep(1)
                if scroll_by != 0:
                    self.driver.execute_script(f"window.scrollBy(0, {scroll_by});")
                    #sleep(2)
                l = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            l = False
        return l

    def find_many(self, xpath):
        try:
            m = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, xpath)))
        except TimeoutException:
            m = []
        return m

    def click(self, xpath, scroll=False):
        l = self.find(xpath, scroll)
        #sleep(1)
        ltag = l.tag_name.lower() if l.tag_name else None
        assert ltag in ['input', 'li', 'button', 'span',
                        'a', 'div', 'textarea'], 'xpath did not return proper element'
        l = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        l.click()
        #sleep(3)
        return l

    def click_element(self, element):
        l = element.click()
        sleep(3)
        return l

    # Method to do hover(move_to_elemet) operation before clicking to avoid click interception error.
    def hover_and_click(self, element):
        self.hover(element)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        l = element.click()
        #sleep(3)
        return l

    def input(self, xpath, keys, scroll=False):
        l = self.find(xpath, scroll)
        ltag = l.tag_name.lower() if l.tag_name else None
        # logger.info('found element with tag %s', ltag)
        assert ltag in ['input', 'li', 'button', 'span',
                        'a', 'div', 'textarea'], 'xpath did not return proper element'
        l = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        l.click()
        #sleep(0.1)
        l.send_keys(keys)
        #sleep(0.1)
        return l

    def close_windows(self):
        # close all windows except 0
        while len(self.driver.window_handles) > 1:
            w = self.driver.window_handles[-1]
            self.driver.switch_to.window(w)
            self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def mark_divs(self):
        for d in self.driver.find_elements_by_xpath("//div"):
            self.driver.execute_script(
                "arguments[0]['style']['border']='1px solid black';", d)

    def get_width(self):
        return self.driver.get_window_size()['width']

    def get_height(self):
        return self.driver.get_window_size()['height']

    def is_desktop(self):
        return self.get_width() >= 1024

    def is_mobile(self):
        return self.get_width() < 425

    def is_tablet(self):
        return self.get_width() >= 425 and self.get_width() < 1024

    def get_current_url(self):
        return self.driver.current_url

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def check_horizontal_overflow(self):
        self.driver.execute_script("$(document).scrollLeft(1)")
        return self.driver.execute_script("return $(document).scrollLeft() === 0")

    def hover(self, elem):
        ltag = elem.tag_name.lower() if elem.tag_name else None
        assert ltag in ['li', 'button', 'span',
                        'a', 'div'], 'xpath did not return proper element'
        actions = ActionChains(self.driver)
        actions.move_to_element(elem)
        actions.perform()
        return elem

    def refresh(self):
        return self.driver.refresh()

    def back(self):
        return self.driver.back()

    def switch_tab_next(self, number):
        #sleep(2)
        return self.driver.switch_to.window(self.driver.window_handles[number])

    # method to get the downloaded file name
    def get_downLoadeded_filename(self):
        self.driver.execute_script("window.open()")
        # switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # navigate to chrome downloads
        self.driver.get('chrome://downloads')
        sleep(5)
        return self.driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').href")

    def get_from_local_storage(self, key):
        return json.loads(self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key))

    def set_local_storage(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def clear_local_storage(self):
        self.driver.execute_script("window.localStorage.clear();")

    def get_window_size(self):
        return self.driver.get_window_size()

    def activate_page(self):
        site_element = self.find(xpath='//div[contains(@class, "site-content")]')
        self.hover(site_element)

    def find_by_link_text(self, text, partial=True, scroll=False, scroll_by=0, scroll_to_view='false'):
        try:
            if partial:
                l = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
            else:
                l = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
            if scroll:
                self.driver.execute_script(f"arguments[0].scrollIntoView({scroll_to_view});", l)
                sleep(1)
                if scroll_by != 0:
                    self.driver.execute_script(f"window.scrollBy(0, {scroll_by});")
                    sleep(2)
                if partial:
                    l = self.wait.until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
                else:
                    l = self.wait.until(
                        EC.presence_of_element_located((By.LINK_TEXT, text)))
        except TimeoutException:
            l = False
        return l

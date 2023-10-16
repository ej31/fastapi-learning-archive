import logging
import os
import time
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Browser(object):
    def __init__(self):
        self.driver = None

    def run(self, has_screen: bool = True):
        try:
            caps = DesiredCapabilities.CHROME
            caps['goog:loggingPrefs'] = {'performance': 'ALL'}
            chrome_options = Options()
            if not has_screen:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--window-size=1920x1080")
                chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-site-isolation-trials")
            chrome_options.add_argument(f"lang=ko_KR")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            self.driver.implicitly_wait(3)
        except Exception as e:
            logging.warning(e)

    def page_source(self):
        return self.driver.page_source

    @property
    def page_height(self):
        return self.driver.execute_script("return document.body.scrollHeight")

    def get(self, url):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    @property
    def current_url(self):
        return self.driver.current_url

    def close(self):
        return self.driver.close()

    def implicitly_wait(self, t):
        self.driver.implicitly_wait(t)

    def find_one(self, css_selector, elem=None, waittime=0, by=By.CSS_SELECTOR):
        obj = elem or self.driver
        if waittime:
            WebDriverWait(obj, waittime).until(
                EC.presence_of_all_elements_located((by, css_selector))
            )

        try:
            return obj.find_element(by, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None

    def find_clickable(self, css_selector, elem=None, waittime=10, by=By.CSS_SELECTOR):
        obj = elem or self.driver

        if waittime:
            WebDriverWait(obj, waittime).until(
                EC.element_to_be_clickable((by, css_selector))
            )

        try:
            return obj.find_element(by, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None

    def find_clickables(self, css_selector, elem=None, waittime=10, by=By.CSS_SELECTOR):
        obj = elem or self.driver

        if waittime:
            WebDriverWait(obj, waittime).until(
                EC.element_to_be_clickable((by, css_selector))
            )

        try:
            return obj.find_elements(by, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None

    def find(self, css_selector, elem=None, waittime=0):
        obj = elem or self.driver

        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
                )
        except TimeoutException as e:
            logging.warning(css_selector)
            return None

        try:
            return obj.find_elements(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None

    def find_css_id(self, css_selector, elem=None, waittime=0):
        obj = elem or self.driver
        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
                )
        except TimeoutException as e:
            logging.warning(css_selector)
            return None

        try:
            return obj.find_element_by_css_selector(css_selector)
        except NoSuchElementException as e:
            logging.warning(css_selector)
            return None

    def switch_to_iframe(self, css_selector, elem=None, waittime=10):
        obj = elem or self.driver
        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, css_selector)))
        except TimeoutException as e:
            logging.warning(css_selector)
            return None

    def find_xpath(self, xpath, elem=None, waittime=0):
        obj = elem or self.driver

        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
        except TimeoutException as e:
            logging.warning(f"Timeout, xpath: {xpath}, elem: {elem}")
            return None

        try:
            return obj.find_element_by_xpath(xpath)
        except NoSuchElementException as e:
            logging.warning(xpath)
            return None

    def scroll_down(self, wait=0.3):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(wait)

    def scroll_up(self, offset=-1, wait=2):
        if offset == -1:
            self.driver.execute_script("window.scrollTo(0, 0)")
        else:
            self.driver.execute_script("window.scrollBy(0, -%s)" % offset)
        time.sleep(wait)
    def js_click(self, elem):
        self.driver.execute_script("arguments[0].click();", elem)

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def open_new_tab(self, url):
        self.driver.execute_script("window.open('%s');" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_current_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def __del__(self):
        try:
            self.driver.quit()
        except Exception as e:
            logging.warning("Driver Quited")
            pass

    def execute_script(self, script, args):
        try:
            self.driver.execute_script(script, args)
        except Exception as e:
            logging.exception(e)
            return None

    def wait_redirect(self, comparison_url):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains(comparison_url))
        except TimeoutException:
            print(traceback.print_exc())
            print("wait_redirect >> ?")

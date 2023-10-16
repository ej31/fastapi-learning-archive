import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from kbl_sample.browser import Browser

if __name__ == '__main__':
    _browser = Browser()
    _browser.run()
    _browser.get("https://www.kbl.or.kr/game/schedule-list")

    _button_els = _browser.find("button.pb", waittime=3)
    for _el in _button_els:
        if _el.get_attribute("data-gmkey") is None:
            continue
        print(_el.get_attribute("data-gmkey"))
    print("!")


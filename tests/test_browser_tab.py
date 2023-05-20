import time

from pages.browser_tab import BrowserPage


def test_browser_tab(browser):
    browser_page = BrowserPage(browser)

    browser_page.visit()
    assert len(browser.window_handles) == 1
    browser_page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)


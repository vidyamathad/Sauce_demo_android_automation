from lib.waits import wait_for_element, wait_and_click


class BasePage:


    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return wait_for_element(self.driver, locator, timeout)

    def wait_and_click(self, locator, timeout=10):
        return wait_and_click(self.driver, locator, timeout)

    def wait_and_get_text(driver, locator, by, timeout=15):
        text = wait_for_element(driver, locator, by, timeout).text
        return text

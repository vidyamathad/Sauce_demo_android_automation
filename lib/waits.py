from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, by, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, locator))
    )

def wait_and_click(driver, locator, by, timeout=15):
    element = wait_for_element(driver, locator, by, timeout)
    element.click()
    return element



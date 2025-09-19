from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "14")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("appPackage", "com.saucelabs.mydemoapp.android")
    options.set_capability("appActivity", "com.saucelabs.mydemoapp.android.view.activities.SplashActivity")
    options.set_capability("automationName", "UiAutomator2")

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(30)
    return driver

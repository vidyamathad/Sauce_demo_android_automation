from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


def create_driver(platform="android", cloud="local", username=None, access_key=None):
    if cloud == "sauce":
        if platform.lower() == "ios":
            url = f"https://{username}:{access_key}@ondemand.eu-central-1.saucelabs.com/wd/hub"
            options = XCUITestOptions().load_capabilities({
                "platformName": "iOS",
                "appium:deviceName": "iPhone 15",
                "appium:platformVersion": "18.7",
                "appium:automationName": "XCUITest",
                "app": "sauce-storage:MyDemoAppRN.ipa",
                "sauce:options": {
                    "build": "MyDemoApp iOS Tests",
                    "name": "Catalog Tests on iPhone 15"
                }
            })
            driver = webdriver.Remote(command_executor=url, options=options)
            return  driver

        elif platform.lower() == "android":
            url = f"https://{username}:{access_key}@ondemand.us-west-1.saucelabs.com/wd/hub"
            options = UiAutomator2Options().load_capabilities({
                "platformName": "Android",
                "appium:deviceName": "Android GoogleAPI Emulator",
                "appium:platformVersion": "13.0",
                "appium:automationName": "UiAutomator2",
                "app": "sauce-storage:MyDemoAppRN.apk",
                "sauce:options": {
                    "build": "MyDemoApp Android Tests",
                    "name": "Catalog Tests on Android"
                }
            })
            driver = webdriver.Remote(command_executor=url, options=options)

            return driver
    else:
        raise NotImplementedError("Local driver not implemented for simplicity")

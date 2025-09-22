from appium import webdriver
from appium.options.ios import XCUITestOptions

def create_driver(platform="ios", cloud="sauce", username=None, access_key=None):
    if cloud == "sauce" and platform.lower() == "ios":
        url = f"https://{username}:{access_key}@ondemand.us-east-1.saucelabs.com/wd/hub"
        print(f"url: {url}")

        options = XCUITestOptions().load_capabilities({
            "platformName": "iOS",
            "appium:deviceName": "iPhone 15.4",
            "appium:platformVersion": "18.7",
            "appium:automationName": "XCUITest",
            "app": "sauce-storage:MyDemoAppRN.ipa",
            "sauce:options": {
                "build": "MyDemoApp iOS Tests",
                "name": "Catalog Tests on iPhone 15"
            }
        })
        driver = webdriver.Remote(command_executor=url, options=options)
        return driver

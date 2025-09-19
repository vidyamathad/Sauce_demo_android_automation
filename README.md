Sauce Labs My Demo App – Mobile Automation Testing (Android + iOS)
This repository contains end-to-end automated tests for the Sauce Labs My Demo App

The framework is built using:
Python 3 + Pytest (test runner)
Appium (mobile automation)
Page Object Model (POM) (maintainable test design)
JSON locators (stable element management)
Allure & Pytest-HTML (reporting with screenshots on failure)

Features Automated
Login Page
Valid login
Invalid login
Logout
Product Catalog
Open catalog
Open product details and verify name and price
Cart
Add a product and verify it appears correctly
Sorting
Apply sorting and verify order

Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/sauce-mobile-automation.git
cd sauce-mobile-automation

2. Install Dependencies
pip install -r requirements.txt

3. Install & Run Appium
npm install -g appium
appium --allow-cors



Open Android Studio → AVD Manager → Create emulator (Pixel, Android 13)
Or connect a real Android device (enable USB Debugging)

 Running on iOS
1. Prerequisites
macOS with Xcode installed
CocoaPods installed (brew install cocoapods)
Appium drivers:
appium driver install xcuitest
iOS simulator (e.g., iPhone 14, iOS 16)

2. Configure Desired Capabilities (iOS)
caps = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:deviceName": "iPhone 14",     # or your simulator/device
    "appium:platformVersion": "16.0",
    "appium:app": "<path-to-app>/MyDemoApp.ipa"   # or .app file
}

Run all tests:
pytest -v
Run Android tests only:
pytest -v --platform=android
Run iOS tests only:
pytest -v --platform=ios


Run with HTML report:
pytest -v --html=reports/report.html --self-contained-html


Reports
Pytest-HTML → reports/report.html (pass/fail percentage, logs, screenshots)

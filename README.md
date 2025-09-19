Sauce Labs My Demo App – Mobile Automation Testing IOS
This branch contains end-to-end automated tests for the Sauce Labs My Demo App

The framework is built using:
Python 3 + Pytest (test runner)
Appium (mobile automation)
Page Object Model (POM) (maintainable test design)
JSON locators (stable element management)
Pytest-HTML (reporting with screenshots on failure)

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

Running on iOS
1. Prerequisites
appium driver install xcuitest
iOS simulator

2. Configure Desired Capabilities (iOS)
caps = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:deviceName": "iPhone 15", 
    "appium:platformVersion": "18.7",
    "appium:app": "<path-to-app>/MyDemoApp.ipa"
}

for runing all tests:
pytest -v

for runing iOS tests only:
pytest -v --platform=ios


Run with HTML report:
pytest -v --html=reports/report.html --self-contained-html


Reports
Pytest-HTML → reports/report.html (pass/fail percentage, logs, screenshots)

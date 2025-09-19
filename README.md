Sauce Labs My Demo App – Android Automation Testing.
This repository contains end-to-end automated tests for the Sauce Labs My Demo App (Android)
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
Open product details and verify name asscending order and decending orderand price assending oorder and decending order.
Add a product and verify it appears correctly
Sorting
Apply sorting and verify order.

Setup Instructions
git clone https://github.com/your-username/sauce-android-automation.git
cd sauce-android-automation.

install dependencies 
pip install -r requirements.txt

Install and Run Appium
npm install -g appium
appium --allow-cors

Configure Desired Capabilities
caps = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "emulator-5554",
    "appium:platformVersion": "14",
    "appium:app": "<path-to-apk>/my-demo-app.apk"
}

Running Tests
pytest -v

Run with HTML report:
pytest -v --html=reports/report.html --self-contained-html


Run with Allure report:
pytest -v --alluredir=reports/allure-results
allure serve reports/allure-results

Reports
Pytest-HTML → Generates report.html with pass/fail percentage and error logs
Allure Report → Interactive dashboard with steps, logs, and screenshots

Example command:
pytest -v --html=reports/report.html --self-contained-html --alluredir=reports/allure-results



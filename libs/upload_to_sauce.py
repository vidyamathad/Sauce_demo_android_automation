import requests
import os

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "your-username-here")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY", "your-access-key-here")

app_path = "apps/MyDemoAppRN.ipa"
url = "https://api.eu-central-1.saucelabs.com/v1/storage/upload"

with open(app_path, "rb") as f:
    response = requests.post(
        url,
        auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
        files={"payload": f},
        data={"name": "MyDemoAppRN.ipa"}
    )

print("Upload response:", response.text)

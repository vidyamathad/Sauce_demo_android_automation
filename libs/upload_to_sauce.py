import requests

SAUCE_USERNAME = "USERNAME"
SAUCE_ACCESS_KEY = "KEY"

app_path = "apps/MyDemoAppRN.ipa"
url = "https://api.us-west-1.saucelabs.com/v1/storage/upload"

with open(app_path, "rb") as f:
    response = requests.post(
        url,
        auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
        files={"payload": f},
        data={"name": "MyDemoAppRN.ipa"}  # this becomes sauce-storage:MyDemoAppRN.ipa
    )

print(response.json())

# utils/upload_app.py
import requests
import os

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")


def upload_to_sauce(app_path: str, app_name: str) -> str:
    """
    Uploads .ipa file to Sauce Labs storage and returns the app ID.
    """
    url = f"https://api.us-west-1.saucelabs.com/v1/storage/upload"

    with open(app_path, "rb") as f:
        files = {"file": (app_name, f)}
        response = requests.post(
            url,
            auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
            files=files,
            data={"name": app_name, "overwrite": "true"}
        )
    if response.status_code == 200:
        print("Upload successful!")
        return f"sauce-storage:{app_name}"
    else:
        raise Exception(f"Upload failed: {response.text}")


# Example usage
if __name__ == "__main__":
    app_id = upload_to_sauce(r"apps/MyDemoAppRN.ipa", "MyDemoAppRN.ipa")
    print("App ID for capabilities:", app_id)

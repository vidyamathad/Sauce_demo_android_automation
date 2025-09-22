import requests
import os

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")


def upload_to_sauce(app_path: str, app_name: str) -> str:
    """
    Uploads .ipa file to Sauce Labs storage and returns the app storage reference.
    """
    app_path = "apps/iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.1.ipa"
    url = "https://api.eu-central-1.saucelabs.com/v1/storage/upload"

    # with open(app_path, "rb") as f:
    #     # files = {"payload": f}  # Sauce expects 'payload' not 'file'
    #     response = requests.post(
    #         url,
    #         auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
    #         files=files,
    #         data={"name": app_name, "overwrite": "true"}
    #     )
    #
    # if response.status_code == 200:
    #     print("✅ Upload successful!")
    #     return f"storage:filename={app_name}"
    # else:
    #     raise Exception(f"❌ Upload failed: {response.text}")


    with open(app_path, "rb") as f:
        response = requests.post(
            url,
            auth=(SAUCE_USERNAME, SAUCE_ACCESS_KEY),
            files={"payload": f},
            data={"name": "MyDemoAppRN.ipa", "overwrite": "true"}
        )

    # Check status
    if response.status_code == 200:
        try:
            print(response.json())
        except Exception:
            print("Upload succeeded but response is not JSON:", response.text)
    else:
        print(f"Upload failed! Status code: {response.status_code}")
        print("Response:", response.text)


# Example usage
if __name__ == "__main__":
    app_id = upload_to_sauce("C:/Users/deepa/PycharmProjects/Sauce_demo_ios/apps/", "MyDemoAppRN.ipa")
    print("App ID for capabilities:", app_id)

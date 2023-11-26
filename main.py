import requests


def call_api():
    try:
        res = requests.get(url="https://feedback-json-data-server.onrender.com/")
        print(f"Response from API: {res.status_code}")
    except Exception as e:
        print(f"Error occurred: {e}")


call_api()


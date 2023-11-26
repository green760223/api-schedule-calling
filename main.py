import requests


def call_api():
    res = requests.get(url="https://feedback-json-data-server.onrender.com/")
    print(f"Response from API: {res.status_code}")


call_api()


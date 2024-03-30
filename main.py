import requests


def call_api():
    urls = [
        "https://feedback-json-data-server.onrender.com/db",
        "https://api-proxy-service.onrender.com"
    ]

    for url in urls:
        try:
            res = requests.get(url=url)
            print(f"Response from {url}: {res.status_code}")
        except Exception as e:
            print(f"Error occurred {url}: {e}")


call_api()

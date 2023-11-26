import requests
import schedule
import time


def call_api():
    res = requests.get(url="https://feedback-json-data-server.onrender.com/")
    print(f"Response from API: {res.status_code}")


schedule.every(1).minutes.do(call_api)

# while True:
#     schedule.run_pending()
#     time.sleep(2)
#     print("sleeping...")

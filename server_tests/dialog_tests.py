import json
import secrets
import requests
import rasa


sender = secrets.token_urlsafe(16)
url = "http://localhost:5005/webhooks/rest/webhook"


def post(url, input_data=None):
    data = json.dumps(input_data, ensure_ascii=False)
    data = data.encode(encoding="utf-8")
    r = requests.post(url=url, data=data)
    r = json.loads(r.text)
    return r


while True:
    message = input("Your input ->  ")
    data = {
        "sender": sender,
        "message": message
    }
    print(post(url, data))

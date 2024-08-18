import requests

r = requests.get("http://127.0.0.1:20200/kctf-jr-flag-dc101257887787f62bf17c0ffa02a30735113e4a451e222d2a1835af897f6a3e/")

print(r.text.strip())

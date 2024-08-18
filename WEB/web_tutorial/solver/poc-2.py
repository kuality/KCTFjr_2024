import requests

r = requests.get("http://127.0.0.1:20201", params={"count":1e5+500+2e3})

print(r.text[:r.text.find("}")+1])

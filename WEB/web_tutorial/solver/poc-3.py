import requests

r = requests.get("http://127.0.0.1:20202", params={"admin.check":"1"})

print(r.text[:r.text.find("}")+1])

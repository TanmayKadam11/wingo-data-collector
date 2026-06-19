import requests

r = requests.get(
    "https://draw.ar-lottery01.com/WinGo/WinGo_1M.json",
    timeout=20
)

print(r.status_code)
print(r.text)

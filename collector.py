import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(
    "https://draw.ar-lottery01.com/WinGo/WinGo_1M.json",
    headers=headers,
    timeout=20
)

print(r.status_code)
print(r.text)

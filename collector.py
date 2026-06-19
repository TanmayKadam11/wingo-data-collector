import requests

url = "https://draw.ar-lottery01.com/WinGo/WinGo_1M/GetHistoryIssuePage.json?pageNo=1&pageSize=10"

try:
    r = requests.get(url, timeout=20)

    print("Status:", r.status_code)
    print(r.text[:500])

except Exception as e:
    print("Error:", e)

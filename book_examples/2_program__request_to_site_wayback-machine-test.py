import webbrowser
import requests

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a vear, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archive_snapshots"]["closest"]["url"]
    print("Найти эту копию: ", old_site)
    print("It shoud appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Извините, не удачно вышло. Мы не нашли", site)

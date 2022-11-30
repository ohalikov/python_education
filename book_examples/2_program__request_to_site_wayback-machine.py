import webbrowser
import json
from urllib.request import urlopen
print("ОКей, давайте найдем старый сайт")
site = input("Введите URL сайта: ")
era = input("Введите год, месяц, день, как 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
    old_site = data["archive_snapshots"]["closest"]["url"]
    print("Найти эту копию: ", old_site)
    print("It shoud appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Извините, не удачно вышло. Мы не нашли", site)

from bs4 import BeautifulSoup
import urllib.request as req
import os.path

# XMLをダウンロード
url = "https://www.city.yokohama.lg.jp/kurashi/bousai-kyukyu-bohan/bousai-saigai/bosai/data/data.files/0006_20180911.xml"
savename = "shelter.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoupで解析
xml = open (savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# データを各区ごとに確認
info = {}
for i in soup.find_all("locationinformation"):
    name = i.find('name').string
    ward = i.find('ward').string
    addr = i.find('address').string
    note = i.find('definition').string
    if not (ward in info):
        info[ward] = []
    info[ward].append(name)

# 区ごとに防災拠点を表示
for ward in info.keys():
    print("+", ward)
    for name in info[ward]:
        print("| - ", name)


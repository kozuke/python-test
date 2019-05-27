import csv
import urllib.request
from bs4 import BeautifulSoup

# J1の順位表を含むページのURL
url = 'https://www.nikkansports.com/soccer/jleague/j1/data/standings/'
with urllib.request.urlopen(url) as res:
    html = res.read().decode('UTF-8')
    # BeautifulSoupで扱う
    soup = BeautifulSoup(html, 'html.parser')
    print(type(soup))
    # 順位表のテーブルを指定
    table = soup.find('table', {'class': 'dataTable'})
    # tr要素を抽出→業の塊を抽出
    rows = table.findAll('tr')
    # csvデータの書き込み
    with open('j1ranking.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.string)
            writer.writerow(csvRow)

import urllib.request
import json

url='https://api.nhk.or.jp/v2/pg/list/130/g1/2019-05-24.json?key=7Jhr6gK1Iaooq9eo25vbLWFnuCG0gyrC'

name = '広瀬すず'
# (1) APIからのデータを読み込む
jsondata = urllib.request.urlopen(url).read()
# (2) データのタイプをみるよ
#print(type(jsondata))
# (3) dict型に変換
data = json.loads(jsondata)
# (4) データのタイプをみるよー
#print(type(data))
# (5) 文字列変換の確認だおー
#print(type(json.dumps(data)))
# (6) いい感じにフォーマットするお
#print("{}".format(json.dumps(data, ensure_ascii=False, indent=4)))


#print(type(data))

#print(type(data['list']))

#print(type(data['list']['g1']))

for i in data['list']['g1']:
#    #print("{}".format(json.dumps(i, ensure_ascii=False, indent=4)))
    if name in i['act']:
        print('title:' + i['title'])
        print('start_time:' + i['start_time'])
        print('act:' + i['act'])
    #print(type(i['act']))
    #print(i['act'])


#data['g1']

#print("{}".format(json.dumps(data['list'], ensure_ascii=False, indent=4)))

#print("{}".format(json.dumps(data, ensure_ascii=False, indent=4)))

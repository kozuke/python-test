import pandas as pd

# pandasで作成したCSVファイルを読み込む
with open('j1ranking.csv', 'r') as csv_file:
    df = pd.read_csv(csv_file)
# タブ区切りで出力
df.to_csv('j1ranking.tsv', '\t')

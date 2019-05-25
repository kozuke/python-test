import codecs as cd
import pandas as pd
#xxx = pd.read_csv('csv.csv', encoding="shift-jis") #xxxは適当な変数

with cd.open("csv.csv", "r", "Shift-JIS", "ignore") as csv_file:
    df = pd.read_table(csv_file)

print (df.shape[0])


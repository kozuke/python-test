import codecs

filename = "csv.csv"

with codecs.open(filename, "r", "shift-jis", "ignore").read() as csv:
    rows = csv.split("\r\n")
    data = []

    for row in rows:
        if row == "": continue
        cells = row.split(",")
        data.append(cells)

    for c in data:
        print(c)
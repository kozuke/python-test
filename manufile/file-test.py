# with open('test.txt', 'w+') as f:
#     f.write('test')
#     f.seek(0)
#     print(f.read())

import csv

with open('csvdata.csv', 'w') as csv_file:
    fieldnames = ['field1', 'field2']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

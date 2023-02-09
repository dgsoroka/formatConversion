import csv
import json

data = {}
data['emoji'] = []

with open("emoji_data.csv", newline="", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader, None)
    for i in csvReader:
        print(type(i))
        print(i[0])

        data['emoji'].append({
            'emoji': i[0],
            'unicode': i[1],
            'bytes': i[2],
            'description': i[3]
        })

with open('json.json', 'wt') as outFile:
    json.dump(data, outFile)
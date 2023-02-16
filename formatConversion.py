import csv
import json

# создание пустого словаря для дальнейшей загрузки в него описания объектов как в .json
# русское название в кавычках нужно изменить на свое

data = {}
data['emoji'] = []

# считываем исходный файл

with open("emoji_data.csv", newline="", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader, None)
    for i in csvReader:
        print(type(i))
        print(i[0])

        # создаем структуру, как в json, слова в кавычках меняются на названия столбцов из csv файла

        data['emoji'].append({
            'emoji': i[0],
            'unicode': i[1],
            'bytes': i[2],
            'description': i[3]
        })

# сливаем структуру в файл json

with open('json.json', 'wt') as outFile:
    json.dump(data, outFile)
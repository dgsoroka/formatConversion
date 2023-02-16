import csv
import json
import xml.etree.ElementTree as ET
import re


def convert_row(row):
    return f'''<{titleCSV[0]} = "{row[0]}">
    <{titleCSV[1]}>{row[1]}</{titleCSV[1]}>
    <{titleCSV[2]}>{row[2]}</{titleCSV[2]}>
    <{titleCSV[3]}>{row[3]}</{titleCSV[3]}>
    <{titleCSV[4]}>{row[4]}</{titleCSV[4]}>
    <{titleCSV[5]}>{row[5]}</{titleCSV[5]}>
</{titleCSV[0]}>'''


data = {'car_usage': []}
xmlData = []
titleCSV = []

with open("used_car_dataset.csv", newline="", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    next(csvReader, None)

    for i in csvReader:
        print(type(i))
        print(i[0])

        data['car_usage'].append({
            'car_name': i[0],
            'car_price_in_rupees': i[1],
            'kms_driven': i[2],
            'fuel_type': i[3],
            'city': i[4],
            'year_of_manufacture': i[5]
        })
#
with open('json.json', 'wt') as outFile:
    json.dump(data, outFile)

with open('json.json') as jsonFile:
    jsonData = json.load(jsonFile)
    for i in jsonData['car_usage']:
        print('car_name: ', i['car_name'])
        print('car_price_in_rupees:', i['car_price_in_rupees'])
        print('kms_driven: ', i['kms_driven'])
        print('fuel_type: ', i['fuel_type'])
        print('city: ', i['city'])
        print('year_of_manufacture: ', i['year_of_manufacture'])
        print('')

with open("used_car_dataset.csv", newline="", encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    titleCSV = next(csvReader, None)
    for row in csvReader:
        xmlData.append(row)
    print(titleCSV)

with open('xml.xml', 'wt', encoding='utf-8') as xmlFile:
    xmlFile.write('\n'.join([convert_row(row) for row in xmlData]))
print('\n'.join([convert_row(row) for row in xmlData]))

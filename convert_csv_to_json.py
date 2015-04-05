# -*- coding: utf-8 -*-
import csv


with open('thaichildobesityrateage2557.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with open('output.json', 'wb') as jsonfile:
        for each in reader:
            print '"' + each[0] + '": [' + each[4] + ', ' + each[5] + ', ' + each[3] + '], '


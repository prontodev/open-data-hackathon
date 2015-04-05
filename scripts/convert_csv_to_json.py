# -*- coding: utf-8 -*-
import csv


with open('../data/thaichildobesityrateage2557.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for each in reader:
        print '"' + each[0] + '": [' + each[4] + ', ' + each[5] + ', ' + each[3] + '], '


import csv
from datetime import datetime


def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        
        fw = csv.writer(file)
        fw.writerow(data)


writecsv(['gg',50,'19/01/23'])
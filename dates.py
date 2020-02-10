

import csv
import datetime

def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def readMyFile(filename):
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        print("joined,left,difference")
        for row in csvReader:
            if validate(row[12]) and validate(row[15]):
                join = datetime.datetime.strptime(row[12], '%Y-%m-%d')
                left = datetime.datetime.strptime(row[15], '%Y-%m-%d')
                days = abs(left-join).days
                if days < 400:
                    print("%s,%s,%s" % (row[12], row[15], days))

readMyFile('data/people.csv')



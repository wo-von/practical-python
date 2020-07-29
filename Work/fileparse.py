# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename):
    '''
    reads a csv file into a 
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        # read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row: # skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records
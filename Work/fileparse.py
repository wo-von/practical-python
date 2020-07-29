# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types = None):
    '''
    reads a csv file into a 
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        # read the file headers
        headers = next(rows)
        
        if select:
            indices = [headers.index(s) for s in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row: # skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indicesz]
            if types:
                row = [func(value) for func, value in zip(types, row)]
            record = dict(zip(headers, row))
            records.append(record)
    return records
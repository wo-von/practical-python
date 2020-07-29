# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ','):
    '''
    reads a csv file into a 
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delimiter)
        # read the file headers
        if has_headers:
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
            if has_headers:
                if indices:
                    row = [row[index] for index in indicesz]
            if types:
                row = [func(value) for func, value in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records
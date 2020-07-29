# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    reads a csv file into a 
    '''
    if select != None and has_headers == False:
        raise RuntimeError("select argument requires column headers")
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
           
        for n, row in enumerate(rows):
            try:    
                if not row: # skip rows with no data
                    continue
                if has_headers:
                    if indices:
                        row = [row[index] for index in indices]
                if types:
                    row = [func(value) for func, value in zip(types, row)]
                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                    if not silence_errors:
                        print(f"Row {n + 1}: Couldn't convert {row}")
                        print(f"Row {n + 1}: Reason {e}")     
    return records
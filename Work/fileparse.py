# fileparse.py
#
# Exercise 3.3
#-- Standard library
import csv

def parse_csv(filename, select = None, types = None, has_headers = True, delimiter = ',', silence_errors = False):
    '''
    reads a csv iterable into a dictionary (in case there are headers) or into a tuple with raw files. The iterable should be opened and passed by the caller
    '''
    if select != None and has_headers == False:
        raise RuntimeError("select argument requires column headers")
    if type(filename) == str:
        raise RuntimeError("Caller should send the iterator and not the iterable itself")
    rows = csv.reader(filename, delimiter = delimiter)
    # read the file headers
    if has_headers:
        headers = next(rows)
    else:
        headers = []
    if select:
        indices = [headers.index(s) for s in select]
        headers = select
    else:
        indices = []
    records = []
        
    for n, row in enumerate(rows, start = 1):
        try:    
            if not row: # skip rows with no data
                continue
            if select:
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
                    print(f"Row {n}: Couldn't convert {row}")
                    print(f"Row {n}: Reason {e}")     
    return records
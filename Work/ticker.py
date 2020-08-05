#!/usr/bin/python3

##--
# Standard library imports
##--
import csv
##--
# Local imports
##--
from follow import follow

def select_columns(rows, indices):
    for row in rows:
        yield[row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    '''
    gets the output of a generator and returns csv reader object
    '''
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

if __name__ == '__main__':
    # producer
    lines = follow('Data/stocklog.csv')
    # processor
    rows = parse_stock_data(lines)
    # consumer
    for row in rows:
        print(row)
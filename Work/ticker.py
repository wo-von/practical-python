#!/usr/bin/python3

##--
# Standard library imports
##--
import csv
##--
# Local imports
##--
from follow import follow
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield[row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    '''
    gets the output of a generator and returns csv reader object
    '''
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = filter_symbols(parse_stock_data(follow(logfile)), portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        formatter.row([ str(e) for e in row.values()])
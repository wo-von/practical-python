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

def parse_stock_data(lines, portobj, select):
    '''
    gets the output of a generator and returns csv reader object
    '''
    rows = csv.reader(lines)
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, float], row)] for row in rows)
    rows = ({headers: item for headers, item in zip(select, row)} for row in rows)
    rows = (row for row in rows if row['name'] in portobj)
    return rows

def ticker(portfile, logfile, fmt):
    headers = ['name', 'price', 'change']
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile), portfolio, headers)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(headers)
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])
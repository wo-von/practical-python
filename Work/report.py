# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    '''
    opens a given portfolio file and reads it into a list of dictionaries
    '''
    with open(filename) as f:
        portfolio = []
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for row in rows:
            # print(row)
            holding = {}
            holding.update({'name': row[0], 'shares': int(row[1]), 'price' : float(row[2])})
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio

# argv are the argumentsa passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

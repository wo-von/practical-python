# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexted
    '''
    with open(f'Work/{filename}') as f:
        rows = csv.reader(f)
        headers = next(rows)
        totalCost = 0
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(record)
            try:
                # totalCost += int(item[1]) * float(item[2])
                nshares = int(record['shares'])
                price = float(record['price'])
                totalCost += nshares * price
            except ValueError:
                print("Row", rowno, "could not convert", row)
    return totalCost

# argv are the argumentsa passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
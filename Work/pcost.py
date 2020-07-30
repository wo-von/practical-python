# pcost.py
#
# Exercise 1.27

import csv
import sys

import report

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexted
    '''  
    portfolio = report.read_portfolio(filename)
    return sum(s['shares'] * s['price'] for s in portfolio)

# argv are the arguments passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
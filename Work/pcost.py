# pcost.py
#
# Exercise 1.27

import csv
import sys

import fileparse

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexted
    '''
    
    
    portfolio = fileparse.parse_csv(filename, select = ['shares', 'price'], types = [int, float])
    totalCost = 0.0
    for port in portfolio:
        totalCost += port['shares'] * port['price']
    return totalCost

# argv are the arguments passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
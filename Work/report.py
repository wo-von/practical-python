# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename = 'Data/portfolio.csv'):
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

def read_prices(filename = 'Data/prices.csv'):
    '''
    reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        priceDict = {}
        try:
            for row in rows:
                priceDict[row[0]] = float(row[1]) 
        except IndexError:
            pass
    return priceDict
# argv are the argumentsa passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

gainLoss = 0
portfolio = read_portfolio()
prices = read_prices()
for myShares in portfolio:
    if myShares['name'] in prices:
        # print(myShares['name'])
        # print(prices[myShares['name']])
        gainLoss += (myShares['shares'] * (myShares['price'] - prices[myShares['name']]))
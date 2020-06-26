#!/usr/bin/python3
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
def make_report(stockList, priceDic):
    '''
    takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the rows of the form
      Name     Shares      Price     Change
    '''
    report = []
    for item in stockList:
        if item['name'] in priceDic:
            report.append((item['name'], item['shares'], priceDic[item['name']], round(priceDic[item['name']] - item['price'], 2)))
    return report

# argv are the argumentsa passed through the terminal, a list of strings, depending on how many have been passed
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

gainLoss = 0
currentValue = 0
whatIHad = 0
portfolio = read_portfolio()
prices = read_prices()
for myShares in portfolio:
    whatIHad += myShares['shares'] * myShares['price']

for myShares in portfolio:
    # only get the prices, if we have them
    if myShares['name'] in prices:
        currentValue += myShares['shares'] * prices[myShares['name']]
gainLoss = round((whatIHad- currentValue), 2)
# print("Current value of the portfolio", currentValue, "with gain/loss of", gainLoss)
# in 2.11 we assume we have this tuple
headers = ('Name', 'Shares', 'Price', 'Change')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print(f'{10*"-"} {10*"-"} {10*"-"} {10*"-"}')

report = make_report(portfolio, prices)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
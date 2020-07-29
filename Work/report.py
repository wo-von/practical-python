#!/usr/bin/python3
# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename: str = 'Data/portfolio.csv') -> list:
    '''
    opens a given portfolio file and reads it into a list of dictionaries
    '''
    select = ['name', 'shares', 'price']
    operator = [str, int, float]
    with open(filename) as f:
        portfolio = []
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(s) for s in select]
        
        portfolio = [{col:func(row[index]) for col, func, index in zip(select, operator, indices)} for row in rows]
    return portfolio

def read_prices(filename: str = 'Data/prices.csv') -> dict:
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

def make_report(stockList: list, priceDic: dict) -> list:
    '''
    takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the rows of the form
      Name     Shares      Price     Change
    '''
    report = []
    for item in stockList:
        if item['name'] in priceDic:
            report.append((item['name'], item['shares'], priceDic[item['name']], round(priceDic[item['name']] - item['price'], 2)))
    return report

def setPortfolioFile():
    '''
    If filename has been passed through teminal, pass it, if not, use default
    '''
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

# Not sure if this is the correct way to start a program
setPortfolioFile()

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
    price = "$" + str(price)
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
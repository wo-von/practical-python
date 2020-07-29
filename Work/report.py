#!/usr/bin/python3
# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename: str) -> list:
    '''
    opens a given portfolio file and reads it into a list of dictionaries
    '''
    select = ['name', 'shares', 'price']
    type = [str, int, float]
    with open(filename) as f:
        portfolio = []
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(s) for s in select]
        
        portfolio = [{col:fun(row[ind]) for col, fun, ind in zip(select, type, indices)} for row in rows]
    return portfolio

def read_prices(pricesfilename: str) -> dict:
    '''
    reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    '''
    with open(pricesfilename) as f:
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

def print_report(report: list):
    '''
    prints out the report
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')

    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile: str, pricesfile: str):
    '''
    get the filenames for portfolio and prices and trigger are computations and 
    prints out the report
    '''

    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
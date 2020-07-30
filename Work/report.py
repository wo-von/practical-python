#!/usr/bin/python3
# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

from fileparse import parse_csv

def read_portfolio(filename: str) -> list:
    '''
    opens a given portfolio file and reads it into a list of dictionaries
    '''    
    portfolio = parse_csv(filename, select = ['name', 'shares', 'price'], types = [str, int, float])
    return portfolio

def read_prices(pricesfilename: str) -> dict:
    '''
    reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    ''' 
    priceDict = parse_csv(pricesfilename, types = [str, float], has_headers = False)
    return dict(priceDict)

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
#!/usr/bin/python3
# report.py
#
# Exercise 2.4

#-- Standard library
import csv
import sys
from pprint import pprint
#-- Practical python course libraries
import fileparse
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename: str, **opts) -> list:
    '''
    opens a given portfolio file and reads it into a list of Stock instances
    '''    
    with open(filename) as f:
        portdict = fileparse.parse_csv(f, select = ['name', 'shares', 'price'], types = [str, int, float], **opts)
    portfolio = [ Stock(**s) for s in portdict ]
    return Portfolio(portfolio)

def read_prices(pricesfilename: str) -> dict:
    '''
    reads a set of prices such as this into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
    ''' 
    with open(pricesfilename) as f:
        priceDict = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return dict(priceDict)

def make_report(stockList: list, priceDic: dict) -> list:
    '''
    takes a list of Stocks instances and dictionary of prices as input and returns a list of tuples containing the rows of the form
    Name     Shares      Price     Change
    '''
    return [(item.name, item.shares, priceDic[item.name], priceDic[item.name] - item.price) for item in stockList if item.name in priceDic]

def print_report(report: list, formatter: object):
    '''
    prints out the report from a list of (name, shares, price, change)
    tuples
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfoliofile: str, pricesfile: str, fmt = 'html'):
    '''
    get the filenames for portfolio and prices and prepares the report and 
    prints it out
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricesfile)

    # Create the report data
    report = make_report(portfolio, prices)
    
    # print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) == 3:
        portfolio_report(portfoliofile = args[1], pricesfile = args[2])
    else:
        portfolio_report(portfoliofile = args[1], pricesfile = args[2], fmt = args[3])

if __name__ == '__main__':
    if len(sys.argv) not in {3, 4}:
        raise SystemExit(f'usage {sys.argv[0]} portfile pricefile {{format}}')
    main(sys.argv)
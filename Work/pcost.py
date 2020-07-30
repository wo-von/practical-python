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
def main(args):
    '''
    main function, gets commans line arguments are arguments
    '''
    cost = portfolio_cost(args[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'usage {sys.argv[0]} portfile')
    main(sys.argv)
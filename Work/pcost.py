# pcost.py
#
# Exercise 1.27

#-- Standard library
import csv
import sys
#-- Practical python course libraries
import report

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexted
    '''  
    portfolio = report.read_portfolio(filename)
    return sum(s.shares * s.price for s in portfolio)

# argv are the arguments passed through the terminal, a list of strings, depending on how many have been passed
def main(args):
    '''
    main function, gets command line arguments
    '''
    print('Total cost:', portfolio_cost(args[1]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'usage {sys.argv[0]} portfile')
    main(sys.argv)
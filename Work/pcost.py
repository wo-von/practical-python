# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexted
    '''
    with open(f'Work/{filename}') as f:
        rows = csv.reader(f)
        header = next(f)
        stockData = []
        for line in rows:
            # csv reader does much of the stuff itself, no need to manually do them
            # line = line.strip()
            stockData.append(line)
    totalCost = 0
    for item in stockData:
        try:
            totalCost += int(item[1]) * float(item[2])
        except:
            continue
    return totalCost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
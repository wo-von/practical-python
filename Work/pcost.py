# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    '''gets a csv file of the shares, their qunatity and value
    returns the total cost for buying them all
    has a header which should be nexed
    '''
    with open('Work/Data/portfolio.csv', 'rt') as f:
        header = next(f)
        stockData = []
        for line in f:
            line = line.strip()
            stockData.append(line.split(','))
    totalCost = 0
    for item in stockData:
        totalCost += int(item[1]) * float(item[2])
    return totalCost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
# pcost.py
#
# Exercise 1.27

with open('Work/Data/portfolio.csv', 'rt') as f:
    header = next(f)
    stockData = []
    for line in f:
        line = line.strip()
        stockData.append(line.split(','))


totalCost = 0
for item in stockData:
    totalCost += int(item[1]) * float(item[2])
print("Total cost %.2f" % totalCost)
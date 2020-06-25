prices = {} # Initial empty dict

with open('Data/prices.csv', 'rt') as f:
    for line in f:
        try:
            row = line.strip()
            row = row.split(',')
            prices[row[0]] = float(row[1])
        except IndexError:
            pass

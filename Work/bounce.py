# bounce.py
#
# Exercise 1.5

height = 100.0

drops = 1

while drops <= 10:
    
    height = round(height * 3 / 5, 4)
    print(drops, height)
    drops += 1
    

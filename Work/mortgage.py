# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
totalPaid = 0.0
EXTRA_PAYMENT_START_MONTH = 1
EXTRA_PAYMENT_END_MONTH = 12
EXTRA_PAYMENT = 1000.0
monthCounter = 0

# while EXTRA_PAYMENT_DURATION > 0:
#     principal = principal * ( 1 + rate/12) - payment - EXTRA_PAYMENT
#     totalPaid += (payment + EXTRA_PAYMENT)
#     EXTRA_PAYMENT_DURATION -= 1
#     monthCounter += 1

while principal > 0:
    
    if monthCounter >= EXTRA_PAYMENT_START_MONTH and monthCounter <= EXTRA_PAYMENT_END_MONTH:
        if principal <= payment + EXTRA_PAYMENT:
            totalPaid += principal + EXTRA_PAYMENT
            principal -= principal + EXTRA_PAYMENT
        else:
            principal = principal * ( 1 + rate/12) - payment - EXTRA_PAYMENT
            totalPaid += payment + EXTRA_PAYMENT
    else:
        if principal <= payment:
            totalPaid += principal
            principal -= principal
        else:
            principal = principal * ( 1 + rate/12) - payment
            totalPaid += payment
    monthCounter += 1
    # Use sting formating from 01/04  to better align the floating numbers and force a decimal number
    print(monthCounter, f'{totalPaid:<.2f}', f'{principal:<.2f}')

totalPaid = round(totalPaid, 2)
print("total amount paid is", totalPaid, "and it was paid over",monthCounter,"months")
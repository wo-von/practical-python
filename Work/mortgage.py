# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
totalPaid = 0.0
EXTRA_PAYMENT_START_MONTH = 49
EXTRA_PAYMENT_END_MONTH = 109
EXTRA_PAYMENT = 1000.0
monthCounter = 0

# while EXTRA_PAYMENT_DURATION > 0:
#     principal = principal * ( 1 + rate/12) - payment - EXTRA_PAYMENT
#     totalPaid += (payment + EXTRA_PAYMENT)
#     EXTRA_PAYMENT_DURATION -= 1
#     monthCounter += 1

while principal > 0:
    
    if monthCounter >= EXTRA_PAYMENT_START_MONTH and monthCounter <= EXTRA_PAYMENT_END_MONTH:
         principal = principal * ( 1 + rate/12) - payment - EXTRA_PAYMENT
         totalPaid += payment + EXTRA_PAYMENT
    else:
        principal = principal * ( 1 + rate/12) - payment
        totalPaid += payment
    monthCounter += 1
    print(monthCounter, round(totalPaid,2), round(principal,2))

totalPaid = round(totalPaid, 2)
print("total amount paid is", totalPaid, "and it was paid over",monthCounter,"months")
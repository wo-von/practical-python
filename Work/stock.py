#!/usr/bin/python3

class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        print(self.price * self.shares)
    def sell(self, sold):
        self.shares -= sold
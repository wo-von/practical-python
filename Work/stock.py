#!/usr/bin/python3

class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @property
    def cost(self):
        return self.shares * self.price
    def sell(self, sold):
        self.shares -= sold
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
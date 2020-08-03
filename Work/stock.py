#!/usr/bin/python3

class Stock(object):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @property
    def cost(self):
        return self.shares * self.price
    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('shares must be an int')
        self._shares = value
    def sell(self, sold):
        self.shares -= sold
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
#!/usr/bin/python3
from typedproperty import typedproperty, String, Integer, Float

class Stock(object):
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)
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
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
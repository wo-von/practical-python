#!/usr/bin/python3
# portfolio.py

class Portfolio(object):
    '''
    wrapper around list of Stock objects
    '''
    def __init__(self, holdings):
        self._holdings = holdings
    def __iter__(self):
        return self._holdings.__iter__()
    def __len__(self):
        return len(self._holdings)
    def __getitem__(self, index):
        return self._holdings[index]
    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)
    def __repr__(self):
        return f'Portfolio({self._holdings})'
    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.tabulate_shares
        return total_shares
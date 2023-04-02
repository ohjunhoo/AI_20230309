# portfolio.py

import fileparse
from stock import Stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines, 
                                        select=['name','shares','price'], 
                                        types=[str,int,float],
                                        **opts)
        
        self._holdings.append([Stock(d["name"],d["shares"],d["price"]) for d in portdicts])
    # your code here after making stock class using portdicts
        def cls():
            return self._holdings
        return self

    def append(self, holding):
        self.holding = holding
        self._holdings.append(self.holdng)
    # your code here

    @property
    def total_cost(self):
        return sum([s.cost() for s in self._holdings])
    # your code here
        
    

'''
    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

 

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
'''


        

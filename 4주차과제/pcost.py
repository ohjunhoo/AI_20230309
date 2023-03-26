import report
from stock import Stock

def pcost(filename):
    portfolio = report.read_portfolio(filename)
    
    my_portfolio = [Stock(d["name"], d["shares"],d["price"]) for d in portfolio]
    return sum([s.cost()for s in my_portfolio])

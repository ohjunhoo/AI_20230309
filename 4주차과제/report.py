import csv
from stock import Stock

def read_portfolio(filename):
    with open(filename) as f:
        result=[]
        rows = csv.reader(f)
        for row in rows:
            stocks={
                "name" : row[0],
                "shares": row[1],
                "price" : row[2]
            }
            result.append(stocks)
        portfolio=[]    
        for i in range(1,len(result)):
           stock={
            "name": result[i]["name"],
            "shares":int(result[i]["shares"]),
            "price" :float(result[i]["price"])
           }
           portfolio.append(stock)
        return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices =  {}
        rows = csv.reader(f)
        for row in rows:
            prices[row[0]] = float(row[1])
            
        return prices

def make_report_data(portfolio, prices):
    result=[]
    for i in range(len(portfolio)):
        rows={
            "name" : portfolio[i]["name"],
            "shares": portfolio[i]["shares"],
            "price" : prices[portfolio[i]["name"]],
            "change": prices[portfolio[i]["name"]]-portfolio[i]["price"]
        }
        result.append(rows)
    return result

def print_report(reportdata):

    headers = ('Name','Shares','Prics','Change')
    print('%10s %10s %10s %10s' % headers)   
    print(('-' * 10 +' ')*len(headers))
    for row in reportdata:
        print("%10s %10d %10.2f %10.2f" % (row["name"],row["shares"],row["price"], row["change"]))

def portfolio_report(portfoliofile, pricefile):

    portfoliofile = read_portfolio(portfoliofile)
    pricefile = read_prices(pricefile)
    reportdata = make_report_data(portfoliofile, pricefile)
    print_report(reportdata)




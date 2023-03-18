"""
    # Pre-condition
        1. Name
        2. shares
        3. price
        4. updated price
    # Method
        1. csv
        2. csv.reader
        3. for
        4. dictionary
        5.list
        6.list.append()
        7.list.remove()
        8.if
        9.else
    # Post
        1. csv 파일 읽어오고 for를 통해서 각각 name, shares, price라는 키를 가진 값을 만든다.
        2. price와 updated price를 비교해서 같다면 price 같지 않다면 updated price를 배치
        3. 변경된 price와 shares를 * 연산자를 사용해서 Total value를 구한다. 
"""
import csv

with open("portfolio.csv") as f:
    result=[]
    rows = csv.reader(f)
    for row in rows:
        stocks={
            "name": row[0],
            "shares":row[1],
            "price": row[2],
        }
        result.append(stocks)
    result.remove(result[0])
result

with open("prices.csv") as p:
    result_1=list()
    rows = csv.reader(p)
    for row in rows:
        result_1.append(row)
print(result)
result_1.remove(result_1[30])
result_2=list()
for i in range(len(result)):
    for j in range(len(result_1)):
        if result[i]["name"] in result_1[j][0]:
            result_2.append(result_1[j])
print(result_2)

for i in range(len(result)):
    if float(result[i]["price"]) != float(result_2[i][1]):
         result[i]["price"] = result_2[i][1]
print(result)

print("=========================================================")
print("NAME SHARES PRICE")
for i in range(len(result)):
    print(result[i]["name"], end=" ")
    print(result[i]["shares"], end=" ")
    print(result[i]["price"])
print("=========================================================")    
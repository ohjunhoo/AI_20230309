import csv

with open("portfolio.csv") as f:
    rows= csv.reader(f)
    header =next(rows)
    row1=next(rows)
    row2=next(rows)
    row3=next(rows)
    row4=next(rows)
    row5=next(rows)
    row6=next(rows)
    row7=next(rows)
    
    result=[]
    result.append(row1)
    result.append(row2)
    result.append(row3)
    result.append(row4)
    result.append(row5)
    result.append(row6)
    result.append(row7)
    

with open("prices.csv") as p:
    rows= csv.reader(p)
    
    arr=[]
    row1=next(rows)
    row2=next(rows)
    row3=next(rows)
    row4=next(rows)
    row5=next(rows)
    row6=next(rows)
    row7=next(rows)
    row8=next(rows)
    row9=next(rows)
    row10=next(rows)
    row11=next(rows)
    row12=next(rows)
    row13=next(rows)
    row14=next(rows)
    row15=next(rows)
    row16=next(rows)
    row17=next(rows)
    row18=next(rows)
    row19=next(rows)
    row20=next(rows)
    row22=next(rows)
    row21=next(rows)
    row23=next(rows)
    row24=next(rows)
    row25=next(rows)
    row26=next(rows)
    row27=next(rows)
    row28=next(rows)
    row29=next(rows)
    row30=next(rows)
    
        
    arr.append(row1)
    arr.append(row2)
    arr.append(row3)
    arr.append(row4)
    arr.append(row5)
    arr.append(row6)
    arr.append(row7)
    arr.append(row8)
    arr.append(row9)
    arr.append(row10)
    arr.append(row11)
    arr.append(row12)
    arr.append(row13)
    arr.append(row14)
    arr.append(row15)
    arr.append(row16)
    arr.append(row17)
    arr.append(row18)
    arr.append(row19)
    arr.append(row20)
    arr.append(row21)
    arr.append(row22)
    arr.append(row23)
    arr.append(row24)
    arr.append(row25)
    arr.append(row26)
    arr.append(row27)
    arr.append(row28)
    arr.append(row29)
    arr.append(row30)
    

g_arr=[]
for i in range(len(result)):
        g =result[i][0]
        g_arr.append(g)

c_arr=[]
for i in range(len(g_arr)):
    for j in range(len(arr)):
        if g_arr[i] == arr[j][0]:
            c_arr.append(arr[j])

f_arr=[]
for i in range(len(g)):
    for j in range(len(c_arr)):
        if result[i][2] == c_arr[j][1]:
            f_arr.append(result[i][2])
        else:
            f_arr.append(c_arr[j][1])
f_arr=[]
for i in range(len(result)):
        f_arr.append(result[i][:2])       
            
i_arr=[]
for i in range(len(result)):
    if result[i][2] != c_arr[i][1]:
        i_arr.append(c_arr[i][1])
for i in range(len(f_arr)):
    f_arr[i].append(i_arr[i])
print(c_arr)
print(result)        
print(f_arr)
ff_arr=[]
a=float(f_arr[0][2])
for i in range(len(f_arr)):
    ff_arr.append((int(float(f_arr[i][1])*float(f_arr[i][2]))))
    
print(ff_arr)

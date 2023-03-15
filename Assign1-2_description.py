
#find strobogrammatic in multi digit numbers
#each digit number you will be able to find some rule 
#916  180 deegree  916
#818  180 deegree  818
# tip : 9 and 6 need to be paired 
# n = 1 {0, 1, 8}
# n = 2 {11, 88, 69, 96}
# n = 3 {}
def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = recursive(n, n)
    return result


def recursive(n, length):
    if n == 0:
        return[""]
    if n == 1 :
        return["0","1","8"]
    middles = recursive(n-2, length)
    
    result=[]
    for m in middles:
        if n != length:
            result.append("0"+m+"0")
        result.append("1"+m+"1")
        result.append("6"+m+"6")
        result.append("8"+m+"8")
        result.append("9"+m+"6")

    return result
            
print("n = 3: \n",gen_strobogrammatic(3))

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T=70
result=[]
for i in X:
    for j in Y:
        for n in Z:
            result.append(i+j+n)
result_1=[]
result= list(set(result))
for i in result:
    if i == T:
        result_1.append(True)
    else:
        result_1.append(False)  

result_1=tuple((result_1))
print(result)
print(result_1)


          
          
          
          
          
          
          
          
          
          
          
          


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


          
          
          
          
          
          
          
          
          
          
          
          

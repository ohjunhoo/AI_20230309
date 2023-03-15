#3개의 배열에서 3개의 요소(각각 배열에서)의 합이 목표 값과 같은지 확인하는 
#Python 프로그램을 작성하십시오. 
#3요소 조합을 모두 인쇄하십시오.
'''
샘플 데이터:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
목표 = 70
*/
'''
import itertools
from functools import partial
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70


#중복되지 않은 List를 만든 후에 
#sum 이 타켓값과 같은 경우 True 아닐 경우 False를 Tuple로 Return 한다
def check_sum_array(N, *nums): 
    
 
    #itertool return combination of X Y and Z
    pro = itertools.product(X,Y,Z)
    print(list(pro))

    #mapping T = 70
    func = partial(check_sum_array, T)

    #func 아래 mapping *nums 리턴 한다 
    sums = list(itertools.starmap(func, pro))

    #Sava list if sum is T(70)

            
            
            
            
            
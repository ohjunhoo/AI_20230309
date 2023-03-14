# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:03:23 2016

@author: ericgrimson
"""

"""
    Pre-condition
        1. x =int(input())
        2. x % 2 == 0
        3. x % 2 != 0
    Method
        1.input
        2.int
        3.if
        4.else
    Post
        1.input을 사용해서 x 값을 입력받고 int()를 사용해서 형변환을 시켜준다.
            //input으로 입력된 값은 항상 문자열이기 때문이다.
        2.if와 else를 사용해서 입력받은 값이 짝수인지 홀수인지 판별하고
          짝수인 경우 "Even"을 출력
          홀수인 경우 "Odd "를 출력한다.
        3.마지막으로 "Done with conditional"을 출력한다.
        
"""
x = int(input('Enter an integer: '))
if x%2 == 0:
    print('')
    print('Even')
else:
    print('')
    print('Odd')
print('Done with conditional')



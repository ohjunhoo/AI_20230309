# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:07:33 2016

@author: ericgrimson
"""
"""
    Pre-condition
        1. x = int(input())
        2. x % 2 == 0 and x % 3 == 0
        3. x % 2 ==0
        4. x % 3 == 0
    Method
        1. if
        2. else
    Post
        1. x가 짝수이면서 홀수인 경우 "Divisible by 2 and 3"
        2. x가 짝수인 경우 "Divisible by 2 not by 3"
        3. x가 홀수인 경우 "Divisible by 3 not by 2"
"""
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

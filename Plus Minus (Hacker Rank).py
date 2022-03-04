#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    a=0
    b=0
    c=0
    for i in range(n):
        if arr[i]>0:
            a+=1
            continue
        elif arr[i]<0:
            b+=1
            continue
        elif arr[i]==0:
            c+=1
            continue
    print(a/n)
    print(b/n)
    print(c/n)            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

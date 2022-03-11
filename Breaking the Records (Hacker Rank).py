#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    a=0
    b=0
    list1=[]
    c=scores[0]
    d=scores[0]
    for i in range(len(scores)-1):
        if c<scores[i+1]:
            a+=1
            c=scores[i+1]
            continue
        else:
             continue  
    for i in range(len(scores)-1):
        if d>scores[i+1]:
            b+=1
            d=scores[i+1]
            continue
        else:
             continue  
    list1.append(a)
    list1.append(b)
    return list1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

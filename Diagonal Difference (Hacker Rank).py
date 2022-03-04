import math
import os
import random
import re
import sys
def diagonalDifference(arr):
    # Write your code here
    z=0
    y=0
    j=n-1
    for i in range(n):
        z+=arr[i][i]
        y+=arr[i][j]
        j-=1
    x=abs(z-y)
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
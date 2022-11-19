# cook your dish here
from collections import Counter
for i in range(int(input())):
    int1=int(input())
    list1=list(map(int, input().split()))
    dict1=Counter(list1)
    p=0
    for j,k in dict1.items():
        if k>=3:
            p=1
            print("No")
            break
    if p==0:
        print("Yes")
    
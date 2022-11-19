# cook your dish here
from collections import Counter
for i in range(int(input())):
    int1=int(input())
    str1=input()
    list1=list(str1)
    dict1=Counter(list1)
    p=0
    for j,k in dict1.items():
        if k%2!=0:
            p=1
            print("NO")
            break
    if p==0:
        print("YES")
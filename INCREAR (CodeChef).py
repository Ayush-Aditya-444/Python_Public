import math
g=int(input())
for v in range(g):
    d,s=input().split()
    d=int(d)
    s=int(s)
    if d!=s:
        if d<s:
          print (s-d)
        elif s<d :
          if(d-s)%2==0:
            print((d-s)//2)
          else:
            print((d-s)//2+(d-s)%2+1)
    else:
        print("0")
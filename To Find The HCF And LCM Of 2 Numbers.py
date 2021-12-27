import math
a=int(input("Enter Your First Number:- "))
b=int(input("Enter Your Second Number:- "))
if a>b:
    c=a
else:
    c=b
for i in range(2,c):
    if a%i==0 and b%i==0:
        d=i
    else:
        d=1
print(f"GCD Of The 2 Numbers Are= {d}")
e=(a*b)/d
print(f"LCM Of The 2 Numbers Are= {e}")
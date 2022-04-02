# cook your dish here
a,b,c=map(int, input().split())
d=(20-b)*6*6
if a>=d+c:
    print("No")
else:
    print("Yes")
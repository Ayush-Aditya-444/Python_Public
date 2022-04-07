# cook your dish here
a,b,c=map(int, input().split())
list1=list(map(int, input().split()))
d=0
for i in range(len(list1)):
    if list1[i]+c>=b:
        d=d+1
if d==0:
    print("NO")
else:
    print("YES")
        
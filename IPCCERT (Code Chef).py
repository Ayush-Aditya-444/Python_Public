a,b,c=map(int, input().split())
z=0
for i in range(a):
    list1=list(map(int, input().split()))
    d=sum(list1)-list1[c]
    if d>=b and list1[c]<=b :
        z+=1
    else:
        continue
print(z)
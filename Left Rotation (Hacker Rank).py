a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=[]
d=a[1]%len(b)
e=b[-1]
for i in range(a[1]-1):
    if b[i]!=e & len(b)==len(c):
        c.append(b[i+e])
    elif b[i]==e:
        i=0
print(c)
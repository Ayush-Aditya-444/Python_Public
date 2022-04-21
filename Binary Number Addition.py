a=str(input())
b=str(input())
j=len(a)-1
k=len(b)-1
z=0
y=0
for i in range(len(a)):
    if a[i]=="1":
        z=z+pow(2,j)
        j=j-1
    else:
        j=j-1
        continue
print("z value",z)
for l in range(len(b)):
    if b[l]=="1":
        y=y+pow(2,k)
        k=k-1
    else:
        k=k-1
        continue
print("y value",y)
h=z+y
print("Sum",h)
list1=[]
while h>0:
    m=h%2
    m=str(m)
    list1.append(m)
    h//=2
list1.reverse()
print("".join(list1))
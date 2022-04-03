a=input()
b=int(input())
c=""
d=""
list1=[]
list2=[]
j=0
for i in range(b):
    list1.append(a[i])
    list2.append(a[(j-1)])
    j=j-1
d=d.join(list2)
c=c.join(list1)
print(d)
print(c)

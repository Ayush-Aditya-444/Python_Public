# a=str(input())
# b=str(input())
# sum=bin(int(a, 2) + int(b, 2))
# print(sum[2:])
def Binary(d):
   if d>=1:
       Binary(d// 2)
   print(d%2, end = '')  
  
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
        continue
for l in range(len(b)):
    if b[l]=="1":
        y=y+pow(2,j)
        k=k-1
    else:
        continue
h=z+y
Binary(h)

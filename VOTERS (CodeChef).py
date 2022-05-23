# cook your dish here
a,b,c=map(int,input().split())
n=a+b+c
l1=[]
l2=[]
z=n
for i in range(n):
    l1.append(int(input()))
l1.sort()
i=0
while(i<z):
    m=0
    j=i+1
    while(j<n and l1[i]==l1[j]):
        m=m+1
        j=j+1
    if m!=0:
        l2.append(l1[i])
    i=j
    
        
print(len(l2))
for i in range(len(l2)):
    print(l2[i])
   

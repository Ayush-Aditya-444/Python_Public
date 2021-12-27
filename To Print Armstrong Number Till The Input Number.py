a=int(input("Enter A Number: "))
b=0
print(0)
for i in range(1,a+1):
    j=i
    while j>0:
        d=j%10
        b+=d**3
        j//= 10
    if i==b:
        print(i)
    b=0
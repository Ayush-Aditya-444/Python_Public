a=int(input("Enter A Number: "))
b=0
c=a
while c>0:
   d=c%10
   b+=d**3
   c//= 10
if a==b:
   print(a,"is an Armstrong number")
else:
   print(a,"is not an Armstrong number")
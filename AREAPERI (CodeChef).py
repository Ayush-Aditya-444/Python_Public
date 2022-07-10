# cook your dish here
a=int(input())
b=int(input())
num1=a*b
num2=2*(a+b)
if num1==num2:
    print("Eq")
    print(num1)
elif num1>num2:
    print("Area")
    print(num1)
else:
    print("Peri")
    print(num2)
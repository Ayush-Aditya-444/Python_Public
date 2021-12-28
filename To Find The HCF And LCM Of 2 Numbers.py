import math
a = int(input("Enter Your First Number:- "))
b = int(input("Enter Your Second Number:- "))
num1 = a
num2 = b
while True:
    if b == 0:
        print(a)
        break
    else:
        a, b = b, a % b

print(f"GCD Of The 2 Numbers Are= {a}")
e = int((num1 * num2) / a)
print(f"LCM Of The 2 Numbers Are= {e}")
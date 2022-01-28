print("Sovling Linear Equations With 2 variables:- ")
a=int(input("Enter Coefficient Of X Of 1st Equations:- "))
b=int(input("Enter Coefficient Of Y Of 1st Equations:- "))
z=int(input("Enter Value After Equal To Of 1st Equations:- "))
c=int(input("Enter Coefficient Of X Of 2nd Equations:- "))
d=int(input("Enter Coefficient Of Y Of 2nd Equations:- "))
y=int(input("Enter Value After Equal To Of 2nd Equations:- "))
print("Your Equations Are:-")
print(f"{a}X + {b}Y = {z}  (1st Equations)")
print(f"{c}X + {d}Y = {y}  (2nd Equations)")
e=a*c
f=b*c
x=z*c
g=c*a
h=d*a
w=y*a
print("First Step:-")
print(f"{e}X + {f}Y = {x}  (1st Equations)")
print(f"{g}X + {h}Y = {w}  (2nd Equations)")
print("Second Step:-")
i=f-h
v=x-w
print(f"{i}Y = {v}")
print("Third Step:- ")
j=v/i
print(f"Y = {j}")
print("Fourth Step:- ")
k=z-(b*j)
print(f"X = {k}")
print("Solutions:-")
print(f"X Value = {k}")
print(f"Y Value = {j}")
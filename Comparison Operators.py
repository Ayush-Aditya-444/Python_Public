print("Comparision Operators:-")
x=input("Enter Temperature=")
y=int(x)
if y >35:
    print("Weather Is Hot")
elif y ==35:
    print("Weather Is Good")
else:
    print("Weather Is Cold")
print("Questions:-")
a=input("Enter Your Name= ")
c=len(a)
b=int(c)
if b<3:
    print("Name Must Be Atleast 3 Letters")
elif b>50:
    print("Name Can Be A Maximum Of 50 Characters")
else:
    print("Name Looks Good")
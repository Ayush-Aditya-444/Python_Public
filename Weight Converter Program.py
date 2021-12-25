print("Weight Converter Program:-")
print("In Which Unit You Want To Enter Your Weight")
print("Type 1 For Kilogram")
print("Type 2 For Pounds")
print("Type 3 For Ounce")
z=input("Enter Your Value=")
y=int(z)
if y<=3:
    b=input("Enter You Weight=")
c=int(b)
if y==1:
    d=c*2.20462
    print(f"Weight In Pounds= {d}")
    e=c*35.274
    print(f"Weight In Onces= {e}")
elif y==2:
    d=c*0.453592
    print(f"Weight In Kilogram= {d}")
    e=c*16
    print(f"Weight In Ounces= {e}")
elif y==3:
    d=c*0.02833495
    print(f"Weight In Kilogram= {d}")
    e=c*0.0625
    print(f"Weight In Pounds= {e}")
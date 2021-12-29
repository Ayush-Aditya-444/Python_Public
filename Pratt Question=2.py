print("Enter Your House Co-ordinates:-")
a=int(input("Enter Starting Point Of Your House= "))
b=int(input("Enter End Point Of Your House= "))
print(f"So Your House Starting Point Is {a} and End Point Is {b}.")
c=int(input("Enter Apple Tree Location(On X Axis)= "))
d=int(input("Enter Orange Tree Location(On x Axis)= "))
print(f"So Apple Tree Location Is {c}")
print(f"So Orange Tree Location Is {d}")
e=int(input("No. Of Apples Fallen= "))
f=int(input("No. Of Oranges Fallen= "))
list1=[]
list2=[]
for i in range(e):
    g=int(input(f"Enter Co-ordinates of Apple From Tree {i+1}= "))
    k=c+g
    list1.append(k)
print(list1)
for j in range(f):
    h=int(input(f"Enter Co-ordinates of Orange From Tree {j+1}= "))
    l=d+h
    list2.append(l)
print(list2)
n=0
for m in range(e):
    if a<=list1[m] and b>=list1[m]:
        n=n+1
print(f"No. Of Apples Fallen Outside THE House= {n}")
o=0
for p in range(f):
    if a<=list2[p] and b>=list2[p]:
        o=o+1
print(f"No. Of Oranges Fallen Oustide The House= {o}")
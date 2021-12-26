print("Nested Loop:-")
for i in range(0,3):
    for j in range(0,3):
        print(i,j)
list1=[5,2,5,2,2]
for x in list1:
    print("x"*x)
list2=[5,2,5,2,2]
for y in list2:
    z=''
    for a in range(y):
        z+="x"
    print(z)

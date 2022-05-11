list1=[1,2,3]
list1.append(4)
list1.append(5)
print(list1)
a=list1.pop()
print(a)
print(list1)
list1.pop()
list1.pop()
list1.pop()
list1.pop()
print(list1)
if not list1:
    print("Empty Stack")
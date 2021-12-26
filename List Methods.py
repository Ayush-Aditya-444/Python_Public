from typing import List


print("Lists Methods:-")
print("Examples:-")
Numbers=[3,4,5,7,7,42,343,244234,56,66,4]
Numbers.append(20)#value
print(Numbers)
Numbers.insert(0, 8)#poisition #value
print(Numbers)
Numbers.remove(7)#value
print(Numbers)
Numbers.pop(8)#poisition
print(Numbers)
print(Numbers.index(3))#value
print(42 in Numbers)
print(Numbers.count(7))
Numbers.sort()
print(Numbers)
Numbers.reverse()
print(Numbers)
Numbers2=Numbers.copy()
print(Numbers2)
print("Question:-")
List1=[1,4,5,3,4,3,6,7,8,2,11]
print(List1)
List1.sort()
print(List1)
for i in range(len(List1)):
    for j in range(i+1, len(List1)-1):
        if List1[i]==List1[j]:
            List1.pop(i)
print(List1)
from typing import List


print("List:-\nExamples:-")
Names=['John',"Bob",'Mosh','Sarah','Mary']
print(Names)
print(Names[4])
print(Names[-2])
print(Names[0:4])
print(Names[0:4:2])
Names[0]='Ayush'
print(Names)
print("Question:-\nMethod 1:-")
List1=[22,4,55,7,6,1,99]
print(List1)
List1.sort()
print("Largest Number In The List: ", List1[-1])
print("Method 2:-")
List2=[12,3,55,99,1,45,4]
print(List2)
Max_Number=List2[0]
for number in List2:
    if number>Max_Number:
        Max_Number=number
print(Max_Number)
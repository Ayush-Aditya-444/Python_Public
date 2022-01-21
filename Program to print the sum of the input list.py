list1=[]
sum=0
a=int(input("Enter Number Of Elements You Want In Your List:- "))
for i in range(a):
    list1.append(int(input("Enter The Value = ")))
print("Your List:-")
print(list1)
for i in range(a):
    sum+=list1[i]
print("Sum Of List:-")
print(sum)
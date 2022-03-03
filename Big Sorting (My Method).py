list1=[]
for i in range(int(input())):
    b=int(input())
    list1.append(b)
    list1.sort()
print(*list1, sep = "\n")
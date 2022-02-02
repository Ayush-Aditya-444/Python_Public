a=int(input())
set=[]
set1=[]
for i in range(a):
    set.append(input())
    for i in set:
        if i not in set1:
            set1.append(i)
print(len(set1))
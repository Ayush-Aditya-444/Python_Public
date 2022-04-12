matches = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
for i in range(int(input())):
    a,b = list(map(int,input().split()))
    c = a+b
    res = 0
    for i in str(c):
        res+=matches[i]
    print(res)
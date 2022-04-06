for i in range(int(input())):
        a=int(input())
        string1=list(str(a))
        if sum(list(map(int, string1)))%2==0:
            while (sum(list(map(int, string1)))%2==0):
                a=a+1
                string1=list(str(a))
            print(a)
        else:
            while (sum(list(map(int, string1)))%2!=0):  
                a=a+1
                string1=list(str(a))
            print(a)
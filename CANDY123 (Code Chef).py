for i in range(int(input())):
    max_limak,max_bob=map(int,input().split())
    a=0
    b=0
    count=0
    while a<=max_limak and b<=max_bob:
        count+=1 
        a+=count
        count+=1 
        b+=count
    if(a>max_limak and b>max_bob):
        print('Bob')
    elif(a>max_limak):
        print('Bob')
    else:
        print('Limak')

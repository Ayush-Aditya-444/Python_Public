for _ in range(int(input())):
    l1=[]
    l2=[]
    l1[:0]=input()
    l2[:0]=input()
    count=0
    s=0
    d=0
    for i in range(len(l1)):
        if(l1[i]== "?" or l2[i]=="?"):
            count=count+1
        else:        
            if(l1[i]==l2[i]):
                    s=s+1
            else:
                    d=d+1
    print(d, end =" ") 
    print(d+count)
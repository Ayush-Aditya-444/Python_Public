t=int(input())
for i in range(t):
    N=int(input())
    arr=list(map(int,input().split()))
    
    pos_count=0
    neg_count=0
    for i in arr:
        if i==0:
            continue
        elif i>0:
            pos_count+=1
        else:
            neg_count+=1
    Answer=pos_count*(pos_count-1)//2 + neg_count*(neg_count-1)//2
    print(Answer)
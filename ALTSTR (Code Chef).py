def maxLenBinaryAlternatingSeries(n,s):
    
    ones=0
    zeros=0
    
    for i in range(n):
        
        if int(s[i])==1:
            ones+=1
            
        if int(s[i])==0:
            zeros+=1
            
    
    if(ones<zeros):
        maxLen=2*ones+1
    else:
        maxLen=2*zeros+1
        
    if(ones==zeros):
        maxLen=2*zeros
            
    print(maxLen)
        
    
t=int(input())
for j in range(t):
    n=int(input())
    s=input()
    maxLenBinaryAlternatingSeries(n,s)
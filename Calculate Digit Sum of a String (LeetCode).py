def ayush(s):
    s=list(s)
    z=True
    count1=0
    list1=[]
    global k
    while len(s) > k:
        numslst = []
        for i in range(0,len(s),k):
            numslst.append(s[i:i+k])
            
        temp = ''
        for num in numslst:
            digits = [int(i) for i in num] # calculating digit in form of list
            temp += str(sum(digits)) # calculating sum
        s = temp # making current string as required string
    return s
s="11111222223"
k=3
a=ayush(s)
print(a)
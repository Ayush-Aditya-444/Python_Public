def ayush(arr):    
    count1=0
    int1=len(arr)-1
    p=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==0 and i==len(arr)-1:
            p=1
            continue
        if arr[i]==0 and arr[i+1]==0 and p==1:
            continue 
        if arr[i]==0:
            return -1
        if arr[i]+i>=int1:
            p=0
            continue
        elif arr[i]+i<len(arr):
            p=0
            count1+=1
            int1=i
    return count1+1
arr=[1, 3, 5, 8, 0, 2, 6, 7, 6, 8, 9]
print(ayush(arr))
#Method-1 (Kadane's Algorithm)
def ayush(list1):
    current_sum=0
    max_sum=0
    current_poi=0
    start=0
    end=0
    for i in range(len(list1)):
        current_sum+=list1[i]
        if current_sum>max_sum:
            max_sum=current_sum
            start=current_poi
            end=i
        if current_sum<0:
            current_sum=0
            current_poi=i+1
    if max(list1)<0:
        return max(list1)
    return max_sum,list1[start:end+1]
list1=list(map(int, input().split()))
print(ayush(list1))
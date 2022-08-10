def ayush(nums):
    nums.sort()
    count1=0
    while max(nums)!=0:
        try:
            nums=list(set(nums))
            nums.remove(0)
        except ValueError:
            pass
            int1=min(nums)
            nums = [x - int1 for x in nums]
            count1+=1
            return count1

nums = [1]
a=ayush(nums)
print(a)
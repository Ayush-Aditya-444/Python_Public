def ayush(nums):
        list1=[]
        for i in nums:
            int1=i
            if int1+1 not in nums and int1-1 not in nums:
                list1.append(i)
        return list1
nums = [10,6,5,8]
print(ayush(nums))
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            if 1 in set(nums):
                return len(nums)-1
            else:
                return 0
        list1=[]
        count1=0
        for i in range(len(nums)):
            if nums[i]==1:
                count1+=1
            elif nums[i]==0 and i!=0:
                list1.append(count1)
                count1=0
            elif nums[i]==0 and nums[i+1]!=1:
                count1=0
        list1.append(count1)
        sum1=0
        if len(list1)==1:
            count1=0
            count2=0
            for i in range(len(nums)):
                if nums[i]==1:
                    count1+=1
                    if count2<count1:
                        count2=count1
                else:
                    count1=0
            return count2
        else:
            for i in range(len(list1)-1):
                if sum1<list1[i]+list1[i+1]:
                    sum1=list1[i]+list1[i+1]
            return sum1
                
        
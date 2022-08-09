class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1=0
        count2=0
        list1=[]
        for i in range(len(nums)):
            if nums[i]==1:
                count2+=1
            elif nums[i]==0:
                count1=max(count1,count2)
                count2=0
        return max(count1,count2)

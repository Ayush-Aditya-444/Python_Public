class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count1=0
        count2=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and count2%2==0:
                count1+=1
            else:
                count2+=1
        count2+=1
        if count2%2==0:
            return count1
        else:
            return count1+1
        
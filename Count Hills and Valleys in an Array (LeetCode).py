class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count2=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=0
                count2+=1
        for i in range(count2):
            nums.remove(0)
        count1=0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                count1+=1
            elif nums[i]<nums[i+1] and nums[i]<nums[i-1]:
                count1+=1
        return count1
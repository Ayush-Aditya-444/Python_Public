class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        count1=0
        for i in range(len(nums)//2):
            int1=nums[i]+nums[len(nums)-i-1]
            if int1>count1:
                count1=int1
        return count1
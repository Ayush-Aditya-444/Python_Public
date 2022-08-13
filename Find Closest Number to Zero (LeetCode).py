class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_value=9999999
        min_count=0
        nums.sort()
        for i in range(len(nums)):
            if min_value>=abs(nums[i]):
                min_value=abs(nums[i])
                min_count=nums[i]
        return min_count
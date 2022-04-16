class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=0
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    a=a+1
        return a
        
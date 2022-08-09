class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1,s2=0,sum(nums)
        for i in range(len(nums)):
            s2-=nums[i]
            if s1==s2:
                return i
            s1+=nums[i]
        return -1
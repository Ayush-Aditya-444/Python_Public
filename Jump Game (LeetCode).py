class Solution:
    def canJump(self, nums: List[int]) -> bool:
        int1=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=int1:
                int1=i
        return not int1
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        list1=nums[:]
        nums.sort()
        if nums[-1]>=nums[-2]*2:
            return list1.index(nums[-1])
        else:
            return -1
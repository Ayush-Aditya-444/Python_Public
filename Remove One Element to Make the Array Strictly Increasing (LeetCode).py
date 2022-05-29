class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            list1=nums[:i]+nums[i+1:]
            if sorted(list1) ==list1:
                if len(set(list1))==len(list1):
                    return True
        return False
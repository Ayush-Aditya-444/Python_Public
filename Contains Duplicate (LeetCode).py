class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1=list(set(nums))
        if len(set1)==len(nums):
            return False
        else:
            return True
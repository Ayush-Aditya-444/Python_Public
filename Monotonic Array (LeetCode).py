class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        list1=sorted(nums)
        list2=list1[::-1]
        if nums==list1 or nums==list2:
            return True
        else:
            return False
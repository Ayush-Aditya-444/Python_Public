class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set1=set(nums[0])
        for i in range(len(nums)):
            set2=set(nums[i])
            set1=set1.intersection(set2)
        return sorted(list(set1))
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        else:
            list1=nums[:]
            list1.sort()
            for i in range(len(nums)-k):
                nums.remove(list1[i])
            return nums
        
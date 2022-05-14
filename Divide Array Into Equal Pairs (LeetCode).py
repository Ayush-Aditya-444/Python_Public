class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for ele in set(nums):
            if not nums.count(ele)%2 == 0:
                return False
        else:
            return True
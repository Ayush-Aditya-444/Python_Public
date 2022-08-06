class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        a = nums[0]*nums[1]*nums[2]
        b = nums[0]*nums[-1]*nums[-2]
        return max(a,b)        
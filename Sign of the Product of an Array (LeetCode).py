class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product1=1
        for i in range(len(nums)):
            product1*=nums[i]
        if product1>0:
            return 1
        elif product1<0:
            return -1
        else:
            return 0
        
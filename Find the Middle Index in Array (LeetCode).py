class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            sum1=sum(nums[:i-1])
            sum2=sum(nums[i:])
            if sum1==sum2:
                return i-1
        return -1
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        a=0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    a+=1
        return a
                
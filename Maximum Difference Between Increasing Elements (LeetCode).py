class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        int2=-1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    int1=nums[j]-nums[i]
                    if int1>int2:
                        int2=int1
        return int2
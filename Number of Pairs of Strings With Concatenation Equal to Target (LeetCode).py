class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count1=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        count1+=1
        return count1
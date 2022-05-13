class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count1=0
        for i in range(len(nums)):
            a=str(nums[i])
            if len(a)%2==0:
                count1+=1
        return count1